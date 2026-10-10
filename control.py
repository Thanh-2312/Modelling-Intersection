import math
import random
from vehicle import Vehicle
from generator import TrafficGenerator


class DummyVehicle:
    def __init__(self, s, d=0.0, v=0.0):
        self.s = s
        self.d = d
        self.v = v
        self.L = 0.0
        self.W = 0.0
        self.is_dummy = True
        self.v_type = 'Dummy'
        self.origin = 'Dummy'


class VehicleController:
    def __init__(self):
        # IDM Parameters (Mục 1.5 - AI.md)
        self.T = 1.5       # Thời gian bám đuôi an toàn (s)
        self.delta = 4.0   # Số mũ gia tốc
        self.s0 = 2.0      # Khoảng cách dừng tĩnh tối thiểu (m)
        self.W_road = 21.0 # Bề rộng toàn bộ đường (21m: 3 làn vào + 3 làn ra)
        self.W_half = 10.5 # Nửa bề rộng đường (10.5m)

        # Vị trí dừng nhường đường khi đối đầu tại ngã tư:
        # Xe rẽ trái dừng ở s = -4.0m (vẫn trên phần đường của mình, chưa lấn sang làn đối diện)
        self.LEFT_TURN_WAIT_S = -4.0
        # Xe đi thẳng dừng ở s = -5.0m (trước cung cua rẽ trái, chừa đủ khoảng trống cho xe rẽ trái qua)
        self.STRAIGHT_WAIT_S = -5.0

        # Ngưỡng vận tốc (m/s): xe rẽ trái đi chậm hơn mức này → đang chờ khe hở
        self.LEFT_TURN_BLOCK_SPEED = 2.0
        # Tốc độ tiến từ từ của xe rẽ trái khi tiếp cận ngã tư (m/s) ~ 9.0 km/h
        self.LEFT_TURN_CREEP_SPEED = 3.5
        # Tốc độ đi chậm nhường đường của xe đi thẳng khi có xe rẽ trái (m/s) ~ 10.8 km/h
        self.STRAIGHT_YIELD_SPEED = 3.0

        # Tỉ lệ phân định nhường đường khi 2 xe đối đầu tại ngã tư (Straight vs Left-turn)
        self.P_LEFT_YIELDS = 0.70
        self.P_STRAIGHT_YIELDS = 0.30
        self.conflict_negotiations = {}

        # Thông số điều phối vùng xung đột (Conflict Zone Speed Harmonization):
        self.CZ_HALF_SIZE = 12.0          # Bán kính vùng xung đột (m): [-12, 12]
        self.BASE_CONFLICT_SPEED_CAR = 4.2   # Tốc độ chuẩn qua giao lộ của ô tô (m/s) ~ 15 km/h
        self.BASE_CONFLICT_SPEED_MOTO = 4.8  # Tốc độ chuẩn qua giao lộ của xe máy (m/s) ~ 17 km/h

    def get_conflict_pair_key(self, v1, v2):
        id1, id2 = id(v1), id(v2)
        return (id1, id2) if id1 < id2 else (id2, id1)

    def base_resolve_stochastic_priority(self, v1, v2):
        s1, _ = self.get_frenet_coords(v1)
        s2, _ = self.get_frenet_coords(v2)

        if v1.turn_direction == 'Straight' and s1 > 0.0:
            return v1, v2
        if v2.turn_direction == 'Straight' and s2 > 0.0:
            return v2, v1
        if getattr(v1, 'turn_t', 0.0) > 0.85:
            return v1, v2
        if getattr(v2, 'turn_t', 0.0) > 0.85:
            return v2, v1

        t1 = getattr(v1, 'turn_t', 0.0)
        t2 = getattr(v2, 'turn_t', 0.0)
        if v1.turn_direction == 'Left' and v1.origin != v2.origin and t1 > 0.50:
            return v1, v2
        if v2.turn_direction == 'Left' and v1.origin != v2.origin and t2 > 0.50:
            return v2, v1

        opp_origin1 = {'North': 'South', 'South': 'North', 'East': 'West', 'West': 'East'}.get(v1.origin)
        opp_origin2 = {'North': 'South', 'South': 'North', 'East': 'West', 'West': 'East'}.get(v2.origin)
        if v1.turn_direction == 'Straight' and v2.turn_direction == 'Left' and v2.origin == opp_origin1:
            if (s1 + v1.L / 2.0) > -4.0 and t2 < 0.45:
                return v1, v2
        if v2.turn_direction == 'Straight' and v1.turn_direction == 'Left' and v1.origin == opp_origin2:
            if (s2 + v2.L / 2.0) > -4.0 and t1 < 0.45:
                return v2, v1

        if (s1 > -5.0 and s2 < -8.5):
            return v1, v2
        if (s2 > -5.0 and s1 < -8.5):
            return v2, v1

        w1 = getattr(v1, 'yield_wait_time', 0.0)
        w2 = getattr(v2, 'yield_wait_time', 0.0)
        if w1 > 2.0 and w2 <= 1.5:
            return v1, v2
        if w2 > 2.0 and w1 <= 1.5:
            return v2, v1

        key = self.get_conflict_pair_key(v1, v2)
        if key in self.conflict_negotiations:
            return self.conflict_negotiations[key]['winner'], self.conflict_negotiations[key]['yielder']

        def calc_score(veh, s_pos):
            progress = 0.0
            if getattr(veh, 'nav_state', '') == 'in_intersection':
                progress = 2.5 + getattr(veh, 'turn_t', 0.0) * 2.0
            elif s_pos > -10.5:
                progress = 1.0

            if veh.turn_direction == 'Straight':
                turn_val = 1.5
            elif veh.turn_direction == 'Right':
                turn_val = 0.8
            else:
                turn_val = 0.0

            dist = max(0.0, -s_pos) if s_pos < 0 else 0.0
            v_eff = max(veh.v, 2.5)
            tti_val = -1.0 * (dist / v_eff)

            agg = getattr(veh, 'aggressiveness', 1.0)
            stoch_val = 1.5 * (agg - 1.0)
            type_val = 0.3 if veh.v_type == 'Motorcycle' else 0.0
            wait_time = getattr(veh, 'yield_wait_time', 0.0)
            wait_val = min(wait_time * 2.5, 8.0)

            return progress + turn_val + tti_val + stoch_val + type_val + wait_val

        score1 = calc_score(v1, s1)
        score2 = calc_score(v2, s2)
        delta = score1 - score2 + random.uniform(-0.30, 0.30)
        tau = 0.6
        p1 = 1.0 / (1.0 + math.exp(-max(-8.0, min(8.0, delta / tau))))

        if random.random() < p1:
            winner, yielder = v1, v2
        else:
            winner, yielder = v2, v1

        self.conflict_negotiations[key] = {'winner': winner, 'yielder': yielder}
        return winner, yielder

    def resolve_head_to_head_conflict(self, straight_veh, left_veh):
        s_s, _ = self.get_frenet_coords(straight_veh)
        s_l, _ = self.get_frenet_coords(left_veh)
        front_s = s_s + straight_veh.L / 2.0
        turn_t = getattr(left_veh, 'turn_t', 0.0)

        # 1. Xe đi thẳng đã qua sâu trong giao lộ (front_s > -2.0m): bắt buộc đi tiếp để giải phóng giao lộ!
        if front_s > -2.0:
            return straight_veh, left_veh

        # 2. Xe rẽ trái đã ôm cua sâu qua làn (turn_t >= 0.65): xe rẽ trái ưu tiên thoát cua
        if turn_t >= 0.65:
            return left_veh, straight_veh

        # 3. Xe đi thẳng đã vào ngã tư vượt quá vạch nhường (front_s > -3.5m)
        if front_s > -3.5:
            return straight_veh, left_veh

        # 3. Xe đi thẳng còn ở ngoài vạch nhường (front_s <= -3.5m)
        # và xe rẽ trái đã bắt đầu vào cua (turn_t > 0.30):
        if turn_t > 0.30 and front_s <= -3.5:
            return left_veh, straight_veh

        # 4. Anti-Starvation: xe nào chờ lâu hơn (> 2.0s) được ưu tiên
        w_s = getattr(straight_veh, 'yield_wait_time', 0.0)
        w_l = getattr(left_veh, 'yield_wait_time', 0.0)
        if w_s > 2.0 and w_l <= 1.5:
            return straight_veh, left_veh
        if w_l > 2.0 and w_s <= 1.5:
            return left_veh, straight_veh

        return self.base_resolve_stochastic_priority(straight_veh, left_veh)

    def resolve_stochastic_priority(self, v1, v2):
        s1, _ = self.get_frenet_coords(v1)
        s2, _ = self.get_frenet_coords(v2)

        # Xe đã qua điểm xung đột
        if v1.turn_direction == 'Straight' and s1 > 0.0: return v1, v2
        if v2.turn_direction == 'Straight' and s2 > 0.0: return v2, v1
        if getattr(v1, 'turn_t', 0.0) > 0.85: return v1, v2
        if getattr(v2, 'turn_t', 0.0) > 0.85: return v2, v1

        opp_origin1 = {'North': 'South', 'South': 'North', 'East': 'West', 'West': 'East'}.get(v1.origin)
        if v1.turn_direction == 'Straight' and v2.turn_direction == 'Left' and v2.origin == opp_origin1:
            return self.resolve_head_to_head_conflict(v1, v2)
        if v2.turn_direction == 'Straight' and v1.turn_direction == 'Left' and v1.origin == opp_origin1:
            w, y = self.resolve_head_to_head_conflict(v2, v1)
            return w, y

        return self.base_resolve_stochastic_priority(v1, v2)

    def get_frenet_coords(self, veh):
        """
        Chuyển (x,y) sang (s, d). Dựa vào nhánh đang di chuyển.
        s: Vị trí dọc, d: Độ lệch ngang so với tim đường.
        """
        if hasattr(veh, 'is_dummy'):
            return veh.s, veh.d

        branch = getattr(veh, 'heading_branch', veh.origin)

        if branch == 'West':  # Đi từ Tây sang Đông
            s = veh.x
            d = veh.y
        elif branch == 'East':  # Đi từ Đông sang Tây
            s = -veh.x
            d = -veh.y
        elif branch == 'South':  # Đi từ Nam lên Bắc
            s = veh.y
            d = -veh.x
        elif branch == 'North':  # Đi từ Bắc xuống Nam
            s = -veh.y
            d = veh.x
        else:
            s, d = 0, 0
        return s, d

    def apply_frenet_offset(self, veh, target_d=None, K_p=0.35, dt=0.1):
        """
        Thay đổi góc lái theta mượt mà theo mô hình xe đạp động học (Kinematic Bicycle Model).
        Chỉ dùng khi đi thẳng, đã rẽ xong hoặc đang lách.
        """
        if target_d is None:
            target_d = getattr(veh, 'target_d', -1.75)
        _, current_d = self.get_frenet_coords(veh)
        e = current_d - target_d

        branch = getattr(veh, 'heading_branch', veh.origin)
        base_theta = 0.0
        if branch == 'West':
            base_theta = 0.0
        elif branch == 'East':
            base_theta = math.pi
        elif branch == 'South':
            base_theta = math.pi/2
        elif branch == 'North':
            base_theta = -math.pi/2

        # Lệch góc so với hướng đi chuẩn
        psi = (veh.theta - base_theta + math.pi) % (2 * math.pi) - math.pi

        # Điều khiển vô lăng (steer angle)
        # e âm (đang lệch phải so với target) -> cần bẻ vô lăng sang trái (steer dương)
        steer = -K_p * e - 1.5 * psi
        max_steer = math.radians(28)
        steer = max(-max_steer, min(steer, max_steer))

        wheelbase = 1.3 if veh.v_type == 'Motorcycle' else 2.6
        # Tránh chia cho 0 nếu xe đang đứng yên
        v_steer = max(veh.v, 1.0)
        d_theta = (v_steer / wheelbase) * math.tan(steer) * dt
        veh.theta += d_theta

    def compute_idm(self, ego, lead):
        v = ego.v
        v0 = ego.v_max
        a_max = ego.a_max
        b = abs(ego.a_comf)

        if lead is None:
            return a_max * (1 - (v / v0)**self.delta)

        # Nếu cả 2 xe cùng đang ôm cua trên cùng 1 luồng rẽ (Left hoặc Right):
        if (ego.turn_direction != 'Straight' and getattr(ego, 'turn_t', 0.0) > 0.02 and
            getattr(lead, 'turn_direction', '') == ego.turn_direction and 
            getattr(lead, 'origin', '') == ego.origin):
            dist = math.hypot(lead.x - ego.x, lead.y - ego.y)
            s_gap = dist - (lead.L/2 + ego.L/2)
        else:
            s_ego, _ = self.get_frenet_coords(ego)
            if getattr(lead, 'is_dummy', False):
                s_lead = lead.s
            else:
                s_lead, _ = self.get_frenet_coords(lead)
            s_gap = (s_lead - lead.L/2) - (s_ego + ego.L/2)

        if s_gap <= 0.0:
            s_gap = 0.1

        delta_v = v - lead.v

        s_star = self.s0 + v * self.T + \
            (v * delta_v) / (2 * math.sqrt(a_max * b))
        s_star = max(self.s0, s_star)

        a = a_max * (1 - (v / v0)**self.delta - (s_star / s_gap)**2)
        return a

    def get_lead_vehicle(self, ego, vehicles):
        """
        Tìm xe gần nhất phía trước đang cùng tuyến (heading_branch).
        """
        branch_ego = getattr(ego, 'heading_branch', ego.origin)
        s_ego, d_ego = self.get_frenet_coords(ego)

        min_s_gap = float('inf')
        lead_veh = None

        # 1. Trường hợp ego đang ôm cua rẽ (Left hoặc Right):
        # Tất cả xe cùng origin và cùng turn_direction đều đi trên cùng 1 luồng rẽ duy nhất
        if ego.turn_direction != 'Straight' and getattr(ego, 'turn_t', 0.0) > 0.02:
            min_dist = float('inf')
            t_ego = getattr(ego, 'turn_t', 0.0)
            for v in vehicles:
                if v == ego or getattr(v, 'nav_state', '') == 'departed':
                    continue
                if v.origin == ego.origin and v.turn_direction == ego.turn_direction:
                    t_v = getattr(v, 'turn_t', 0.0)
                    is_ahead = False
                    if getattr(v, 'nav_state', '') in ['leaving', 'departed'] or t_v >= 1.0:
                        is_ahead = True
                    elif t_v > t_ego:
                        is_ahead = True
                    
                    if is_ahead:
                        dist = math.hypot(v.x - ego.x, v.y - ego.y)
                        if dist < 25.0 and dist < min_dist:
                            min_dist = dist
                            lead_veh = v
            return lead_veh

        # 2. Trường hợp đi thẳng hoặc đang tiếp cận nhánh:
        for v in vehicles:
            if v == ego:
                continue
            branch_v = getattr(v, 'heading_branch', v.origin)
            if branch_v != branch_ego:
                continue

            s_v, d_v = self.get_frenet_coords(v)
            if s_v > s_ego:
                s_gap = s_v - s_ego
                same_turn_stream = (ego.turn_direction != 'Straight' and 
                                    v.origin == ego.origin and 
                                    v.turn_direction == ego.turn_direction)
                lat_thresh = max(v.W/2 + ego.W/2 + 0.3, 1.2)
                if same_turn_stream or abs(d_v - d_ego) < lat_thresh:
                    if s_gap < min_s_gap:
                        min_s_gap = s_gap
                        lead_veh = v

        return lead_veh

    def paths_conflict(self, v1, v2):
        if v1.origin == v2.origin:
            return False
        # Nếu cùng nhánh đích: 2 xe nhập chung luồng vào nhánh thoát (Merge conflict)
        if v1.destination == v2.destination:
            return True
        opp_origin = {'North': 'South', 'South': 'North',
                      'East': 'West', 'West': 'East'}[v1.origin]
        if v2.origin == opp_origin:
            if v1.turn_direction == 'Straight' and v2.turn_direction == 'Straight':
                return False
            if v1.turn_direction == 'Right' and v2.turn_direction == 'Straight':
                return False
            if v2.turn_direction == 'Right' and v1.turn_direction == 'Straight':
                return False
            if v1.turn_direction == 'Right' and v2.turn_direction == 'Right':
                return False
            if (v1.turn_direction == 'Right' and v2.turn_direction == 'Left') or \
               (v1.turn_direction == 'Left' and v2.turn_direction == 'Right'):
                return False
            return True
        if v1.turn_direction == 'Right' and v2.turn_direction == 'Right':
            return False
        if v1.turn_direction == 'Right' and v2.turn_direction == 'Straight':
            return False
        if v1.turn_direction == 'Straight' and v2.turn_direction == 'Right':
            return False
        return True

    def get_conflict_vehicle(self, ego, vehicles, signal_controller=None):
        if getattr(ego, 'nav_state', '') in ['leaving', 'departed']:
            return None

        s_ego, _ = self.get_frenet_coords(ego)
        dist_ego = abs(s_ego)
        if dist_ego > 15.0:
            return None

        v_ego_eff = max(ego.v, 3.0)
        t_ego = dist_ego / v_ego_eff

        conflict_dummy = None
        min_t_ego = float('inf')

        opp_origin = {'North': 'South', 'South': 'North',
                      'East': 'West', 'West': 'East'}.get(ego.origin)

        cos_ego = math.cos(ego.theta)
        sin_ego = math.sin(ego.theta)
        front_s_ego = s_ego + ego.L / 2.0
        dist_to_stop = -10.5 - front_s_ego

        for v in vehicles:
            if v == ego or getattr(v, 'nav_state', '') in ['leaving', 'departed']:
                continue
            s_v_conflict, _ = self.get_frenet_coords(v)
            dist_v = abs(s_v_conflict)
            if dist_v > 15.0:
                continue

            v_nav = getattr(v, 'nav_state', 'approaching')

            if ego.nav_state == 'in_intersection' and v_nav == 'approaching':
                continue

            if signal_controller and v_nav == 'approaching':
                if signal_controller.get_state(v.origin) == 'R':
                    continue

            if not self.paths_conflict(ego, v):
                continue

            if v.origin == opp_origin:
                if ego.turn_direction == 'Straight' and v.turn_direction == 'Left':
                    continue
                elif ego.turn_direction == 'Left' and v.turn_direction == 'Straight':
                    continue

            winner, yielder = self.resolve_stochastic_priority(ego, v)
            ego_yields = (ego == yielder)

            if ego_yields:
                is_green = (signal_controller and signal_controller.get_state(ego.origin) == 'G')
                dx = v.x - ego.x
                dy = v.y - ego.y
                s_rel_v = dx * cos_ego + dy * sin_ego

                # Don't Block the Box (HCM Gridlock Prevention):
                is_cross = (v.origin != opp_origin)
                v_at_entry_gate = False
                if is_cross and (getattr(v, 'nav_state', '') == 'in_intersection') and (0.0 < s_rel_v < 8.0):
                    d_rel_v = -dx * sin_ego + dy * cos_ego
                    half_w_ego = ego.W / 2.0 + 0.3
                    half_l_v = v.L / 2.0
                    v_d = -math.sin(ego.theta) * (v.v * math.cos(v.theta)) + math.cos(ego.theta) * (v.v * math.sin(v.theta))
                    has_cleared = False
                    if v_d > 0.1 and (d_rel_v - half_l_v > half_w_ego):
                        has_cleared = True
                    elif v_d < -0.1 and (d_rel_v + half_l_v < -half_w_ego):
                        has_cleared = True
                    if not has_cleared:
                        v_at_entry_gate = True

                wait_too_long = (getattr(ego, 'stopped_green_time', 0.0) > 3.0)

                if is_green and dist_to_stop > 0.0 and v_at_entry_gate and not wait_too_long:
                    yield_s = -10.5
                    dummy = DummyVehicle(s=yield_s, v=0.0)
                    if t_ego < min_t_ego:
                        min_t_ego = t_ego
                        conflict_dummy = dummy
                elif is_green:
                    curr = ego.v_max if getattr(ego, 'v_max_override', None) is None else ego.v_max_override
                    ego.v_max_override = min(curr, 2.0)
                elif ego.nav_state == 'in_intersection':
                    curr = ego.v_max if getattr(ego, 'v_max_override', None) is None else ego.v_max_override
                    ego.v_max_override = min(curr, 2.0)
                elif dist_to_stop > 0.0:
                    yield_s = -10.5
                    dummy = DummyVehicle(s=yield_s, v=0.0)
                    if t_ego < min_t_ego:
                        min_t_ego = t_ego
                        conflict_dummy = dummy

        return conflict_dummy

    def get_defensive_lead(self, ego, vehicles, signal_controller=None):
        """
        Phanh phòng thủ 2D (Defensive Collision Avoidance / AEB) dựa trên TTC dự báo (AI.md mục 4.5.1).
        Quét hành lang an toàn 2D phía trước mũi xe ego kết hợp dự báo thời gian giao cắt [t_start, t_end].
        Nếu có xe cắt ngang hoặc chắn ngang đường, tự động trả về xe ảo để mô hình IDM phanh dừng an toàn.
        """
        closest_gap = float('inf')
        defensive_dummy = None

        cos_ego = math.cos(ego.theta)
        sin_ego = math.sin(ego.theta)
        s_ego, _ = self.get_frenet_coords(ego)

        # Giới hạn tầm nhìn phòng thủ thích ứng để tránh nhìn xuyên qua nút giao gây Deadlock
        if ego.turn_direction != 'Straight':
            # Xe đang hoặc sắp rẽ (đường cong Bezier): tiếp tuyến bị lệch ra ngoài cung cua
            max_s_lookahead = 6.5
        elif getattr(ego, 'nav_state', 'approaching') == 'approaching' and s_ego < -10.5:
            # Xe đang tiếp cận chưa qua vạch dừng: chỉ quan sát mũi xe 8m
            max_s_lookahead = min(max(ego.v * 1.2, 5.0), 8.0)
        else:
            # Xe đi thẳng trong ngã tư: tầm nhìn 12m
            max_s_lookahead = min(max(ego.v * 1.5, 6.0), 12.0)

        for v in vehicles:
            if v == ego or getattr(v, 'nav_state', '') == 'departed':
                continue

            # 1. Bỏ qua xe v đang ở nhánh tiếp cận và bị đèn đỏ chặn (xe đó sẽ dừng trước vạch -10.5m, không cắt mặt)
            if signal_controller and getattr(v, 'nav_state', 'approaching') == 'approaching':
                if signal_controller.get_state(v.origin) == 'R':
                    continue

            # 1.1 Xe ego đang kẹt đèn đỏ trong ngã tư ('in_intersection') có quyền ưu tiên giải phóng ngã tư:
            # Ưu tiên thoát nút, nhưng vẫn phanh phòng thủ khẩn cấp nếu có xe chắn ngay sát trước mũi
            if signal_controller and getattr(ego, 'nav_state', '') == 'in_intersection' and signal_controller.get_state(ego.origin) == 'R':
                if signal_controller.get_state(v.origin) == 'G':
                    dx_chk = v.x - ego.x
                    dy_chk = v.y - ego.y
                    s_rel_chk = dx_chk * cos_ego + dy_chk * sin_ego
                    d_rel_chk = -dx_chk * sin_ego + dy_chk * cos_ego
                    half_w_chk = (ego.W + v.W) / 2.0 + 0.3
                    if abs(d_rel_chk) < half_w_chk and 0.0 < s_rel_chk < 3.5:
                        pass  # Xe chắn trực diện hành lang -> không được đâm, phải phanh an toàn
                    else:
                        continue  # Xe chưa cắt vào hành lang -> Ego tự tin giải phóng nút giao

            # 2. Không phanh nếu 2 quỹ đạo không hề xung đột
            if not self.paths_conflict(ego, v):
                continue

            opp_origin = {'North': 'South', 'South': 'North',
                          'East': 'West', 'West': 'East'}.get(ego.origin)

            # 2.1 Xe đi thẳng đã đi qua tâm ngã tư (s > 1.5m): đã qua điểm giao cắt, không cần phanh nhường xe rẽ trái phía sau
            if ego.turn_direction == 'Straight' and v.origin == opp_origin and v.turn_direction == 'Left':
                s_ego_chk, _ = self.get_frenet_coords(ego)
                if s_ego_chk > 1.5:
                    continue

            # 3. Phân định quyền ưu tiên theo đàm phán ngẫu nhiên (Stochastic Priority Model)
            winner, yielder = self.resolve_stochastic_priority(ego, v)
            # Nếu ego là bên ưu tiên (winner):
            if ego == winner:
                dx_chk = v.x - ego.x
                dy_chk = v.y - ego.y
                s_rel_chk = dx_chk * cos_ego + dy_chk * sin_ego
                d_rel_chk = -dx_chk * sin_ego + dy_chk * cos_ego
                half_w_chk = (ego.W + v.W) / 2.0 + 0.3
                # Nếu ego là xe đi thẳng ưu tiên và xe rẽ trái đối diện đang dừng nhường hoặc chưa cắt vào làn:
                if ego.turn_direction == 'Straight' and v.origin == opp_origin and v.turn_direction == 'Left':
                    s_v_opp, _ = self.get_frenet_coords(v)
                    turn_t_opp = getattr(v, 'turn_t', 0.0)
                    if (s_v_opp + v.L / 2.0) <= -2.5 or turn_t_opp < 0.40 or v.v < 0.5:
                        if abs(d_rel_chk) >= half_w_chk or s_rel_chk > 3.5:
                            continue

                if v.v < 0.5:
                    # Nếu ego là xe rẽ trái đang ôm cua và v là xe đối diện đang dừng nhường:
                    if ego.turn_direction == 'Left' and v.origin == opp_origin:
                        s_v_opp, _ = self.get_frenet_coords(v)
                        if (s_v_opp + v.L / 2.0) <= -3.0:
                            continue
                        t_ego = getattr(ego, 'turn_t', 0.0)
                        if t_ego > 0.50:
                            passed = False
                            # Xe v đã thực sự ở phía SAU lưng xe ego theo chiều thoát cua:
                            if ego.origin == 'East' and v.y > ego.y + 0.2:
                                passed = True
                            elif ego.origin == 'West' and v.y < ego.y - 0.2:
                                passed = True
                            elif ego.origin == 'South' and v.x > ego.x + 0.2:
                                passed = True
                            elif ego.origin == 'North' and v.x < ego.x - 0.2:
                                passed = True
                            if passed:
                                continue
                        # Ngược lại nếu xe đối diện dừng lấn vào cung cua: Ego phanh an toàn không đâm

                    physical_half_w = (ego.W + v.W) / 2.0
                    lookahead_stationary = 2.2 if ego.turn_direction != 'Straight' else 3.2
                    if abs(d_rel_chk) < physical_half_w and 0.0 < s_rel_chk < lookahead_stationary:
                        pass  # Xe yielder đang chắn đường phía trước -> Winner phanh phòng thủ an toàn, không đâm!
                    else:
                        continue  # Xe yielder dừng ngoài hành lang -> Winner đi tiếp
                else:
                    # Xe v đang chuyển động: Winner chỉ phanh khẩn cấp nếu xe v lao tới sát trước mũi (< 3.8m)
                    if s_rel_chk > 3.8:
                        continue
            # Nếu ego là yielder: không skip, cho phép phanh phòng thủ để nhường winner!

            dx = v.x - ego.x
            dy = v.y - ego.y

            # Tọa độ tương đối trong hệ trục cục bộ của ego (Forward / Lateral)
            s_rel = dx * cos_ego + dy * sin_ego
            d_rel = -dx * sin_ego + dy * cos_ego

            # Chỉ quét phía trước trong phạm vi thích ứng (cho phép phát hiện xe cắt ngang/chồng lấn từ s_rel > -0.5m)
            if s_rel <= -0.5 or s_rel > max_s_lookahead:
                continue

            delta_theta = v.theta - ego.theta
            abs_cos = abs(math.cos(delta_theta))
            abs_sin = abs(math.sin(delta_theta))

            # Kích thước hình chiếu của xe v lên hệ trục của ego
            L_v_proj = v.L * abs_cos + v.W * abs_sin
            W_v_proj = v.L * abs_sin + v.W * abs_cos

            # Bề rộng hành lang an toàn theo AI.md mục 4.5.1 Bước 3:
            margin = 0.1
            corridor_half_width = (ego.W + W_v_proj) / 2.0 + margin

            # Vận tốc tương đối chiếu lên hệ trục của ego (Forward & Lateral)
            v_x_rel = v.v * math.cos(v.theta) - ego.v * cos_ego
            v_y_rel = v.v * math.sin(v.theta) - ego.v * sin_ego
            v_rel_s = v_x_rel * cos_ego + v_y_rel * sin_ego
            v_rel_d = -v_x_rel * sin_ego + v_y_rel * cos_ego

            in_corridor_now = abs(d_rel) < corridor_half_width
            will_cross_corridor = False
            t_cross = 0.0
            gap = float('inf')

            if in_corridor_now:
                gap = s_rel - (L_v_proj / 2.0) - (ego.L / 2.0)
            elif abs(v_rel_d) > 0.15:
                # Xe v đang di chuyển cắt ngang vào hành lang của Ego (AI.md Bước 4)
                t1 = (-corridor_half_width - d_rel) / v_rel_d
                t2 = (corridor_half_width - d_rel) / v_rel_d
                t_in = min(t1, t2)
                t_out = max(t1, t2)
                if t_out > 0.0 and t_in < 2.5:
                    t_cross = max(0.0, t_in)
                    s_pred = s_rel + v_rel_s * t_cross
                    # Kiểm tra xem tại thời điểm cắt ngang, xe v có nằm trước mũi ego không
                    if 0.5 < s_pred < 20.0:
                        will_cross_corridor = True
                        gap = s_pred - (L_v_proj / 2.0) - (ego.L / 2.0)

            if in_corridor_now or will_cross_corridor:
                if gap <= 0.0:
                    gap = 0.01  # Đã hoặc sắp chồng chéo → IDM phanh mạnh
                if gap < closest_gap:
                    closest_gap = gap
                    v_longitudinal = max(0.0, v.v * math.cos(delta_theta))

                    dummy_s = s_ego + (s_rel if in_corridor_now else (s_rel + v_rel_s * t_cross))
                    _, d_v = self.get_frenet_coords(v)
                    dummy = DummyVehicle(s=dummy_s, d=d_v, v=v_longitudinal)
                    dummy.L = L_v_proj
                    dummy.W = v.W
                    dummy.v_type = v.v_type
                    dummy._caused_by = v
                    defensive_dummy = dummy

        # Khi ego đang tiếp cận trên đèn XANH chưa qua vạch dừng (s_ego < -10.5):
        # Nếu xe cản trở nằm bên trong giao lộ (defensive_dummy.s > -10.5):
        # KHÔNG dừng chết trước vạch dừng đèn xanh! Cho phép xe bò từ từ vào ngã tư với tốc độ an toàn (2.0 m/s)
        if (defensive_dummy is not None and signal_controller 
                and signal_controller.get_state(ego.origin) == 'G' and s_ego < -10.5):
            if defensive_dummy.s > -10.5:
                curr_cap = ego.v_max if getattr(ego, 'v_max_override', None) is None else ego.v_max_override
                ego.v_max_override = min(curr_cap, 2.0)
                defensive_dummy = None

        if defensive_dummy is not None:
            cb = getattr(defensive_dummy, '_caused_by', None)
            if cb is not None:
                opp_origin = {'North': 'South', 'South': 'North',
                              'East': 'West', 'West': 'East'}.get(ego.origin)

                # Head-to-Head (Opposing Straight vs Left):
                if cb.origin == opp_origin:
                    if ego.turn_direction == 'Left' and cb.turn_direction == 'Straight':
                        winner, yielder = self.resolve_head_to_head_conflict(cb, ego)
                        if ego == winner:
                            return None  # Left turn has priority to clear!
                        # Break deadlock: if cb is stopped (v < 0.2) and ego is already past midpoint (turn_t > 0.50):
                        if cb.v < 0.2 and getattr(ego, 'turn_t', 0.0) > 0.50:
                            return None

                    elif ego.turn_direction == 'Straight' and cb.turn_direction == 'Left':
                        s_ego_chk, _ = self.get_frenet_coords(ego)
                        front_s = s_ego_chk + ego.L / 2.0
                        winner, yielder = self.resolve_head_to_head_conflict(ego, cb)
                        if ego == winner:
                            # Straight ego has priority over oncoming left!
                            # If left is not yet across ego's lane (turn_t <= 0.70 or cb.v < 0.3), Straight clears!
                            if getattr(cb, 'turn_t', 0.0) <= 0.70 or cb.v < 0.3:
                                return None
                        if cb.v < 0.2 and front_s > -3.5:
                            return None

        return defensive_dummy
    def compute_lateral_swerving(self, ego_moto, lead_car, dt=0.1):
        """
        Lách ngang cho xe máy khi gặp ô tô đi chậm phía trước cùng chiều.
        Hỗ trợ chuyển hẳn sang làn trống bên cạnh thay vì phải quay về làn xuất phát.
        CHỈ cho phép lách khi đã vượt qua vạch dừng đèn xanh đèn đỏ (s_ego >= -10.5m).
        """
        if getattr(lead_car, 'is_dummy', False):
            return False

        s_ego, d_ego = self.get_frenet_coords(ego_moto)
        # TUYỆT ĐỐI KHÔNG LÁCH KHI CHƯA QUA VẠCH DỪNG ĐÈN XANH ĐÈN ĐỎ
        if s_ego < -10.5:
            return False

        s_lead, d_lead = self.get_frenet_coords(lead_car)
        s_gap = (s_lead - lead_car.L/2) - (s_ego + ego_moto.L/2)

        if s_gap > 25.0 or s_gap < -0.5:
            return False

        # Ranh giới đường 3 làn (tổng chiều rộng nửa đường là 10.5m)
        d_left_bound = 0.0      # Tim đường
        d_right_bound = -10.2   # Lề phải / vỉa hè (10.2m)

        car_left_edge = d_lead + lead_car.W/2
        car_right_edge = d_lead - lead_car.W/2

        gap_left = d_left_bound - car_left_edge
        gap_right = car_right_edge - d_right_bound
        req_gap = ego_moto.W + 0.4
        target_d = None

        # Ưu tiên chọn làn hợp lệ gần nhất (Lane 2: -5.25, Lane 3: -8.75)
        if gap_right >= req_gap and gap_left >= req_gap:
            if gap_right >= gap_left:
                target_d = car_right_edge - req_gap/2
            else:
                target_d = car_left_edge + req_gap/2
        elif gap_right >= req_gap:
            target_d = car_right_edge - req_gap/2
        elif gap_left >= req_gap:
            target_d = car_left_edge + req_gap/2

        if target_d is not None:
            min_d = d_right_bound + ego_moto.W / 2 + 0.1
            max_d = d_left_bound - ego_moto.W / 2 - 0.1
            target_d = max(min_d, min(target_d, max_d))

            # Chuyển hẳn target_d sang làn hợp lệ gần nhất
            valid_straight_lanes = [-5.25, -8.75]
            nearest_valid_lane = min(valid_straight_lanes, key=lambda l: abs(target_d - l))
            # Kiểm tra nghiêm ngặt hai bên sườn xem có xe hay không trước khi lách
            if self.is_lateral_gap_clear(ego_moto, nearest_valid_lane, [lead_car]):
                ego_moto.target_d = nearest_valid_lane
                ego_moto._exit_lane = abs(nearest_valid_lane)
                self.apply_frenet_offset(ego_moto, ego_moto.target_d, dt=dt)

                lateral_clearance = abs(d_ego - d_lead) - (ego_moto.W/2 + lead_car.W/2)
                if lateral_clearance >= 0.2:
                    return True
        return False

    def is_lateral_gap_clear(self, ego, target_d, vehicles):
        """
        Kiểm tra an toàn hai bên sườn (Lateral Clearance) trước khi lách:
        - Đảm bảo KHÔNG có xe ở sườn cần lách tới để tránh va quẹt vào hai bên.
        - Quét toàn bộ dải dịch chuyển ngang từ vị trí hiện tại (d_ego) sang làn mục tiêu (target_d).
        - Quét cả hệ tọa độ 2D thực tế (tránh xe đang rẽ hoặc cắt ngang) và Frenet cùng luồng.
        """
        s_ego, d_ego = self.get_frenet_coords(ego)
        cos_ego = math.cos(ego.theta)
        sin_ego = math.sin(ego.theta)

        lat_shift = target_d - d_ego
        if abs(lat_shift) < 0.1:
            return True

        d_sweep_min = min(d_ego, target_d) - (ego.W / 2.0 + 0.3)
        d_sweep_max = max(d_ego, target_d) + (ego.W / 2.0 + 0.3)

        for v in vehicles:
            if v == ego or getattr(v, 'nav_state', '') == 'departed':
                continue

            # 1. Quét không gian 2D theo hướng tiến và hướng ngang của Ego
            dx = v.x - ego.x
            dy = v.y - ego.y
            s_rel = dx * cos_ego + dy * sin_ego
            d_rel = -dx * sin_ego + dy * cos_ego

            # Khoảng cách dọc nguy hiểm: sát sườn hoặc chồng lấn thân xe (-2.5m đến +3.5m)
            if -2.5 < s_rel < (ego.L / 2.0 + v.L / 2.0 + 2.5):
                # Xe v nằm ở phía sườn mà Ego định lách tới:
                if lat_shift < 0:  # Lách sang phải (d âm hơn)
                    if -(abs(lat_shift) + v.W / 2.0 + 0.4) <= d_rel <= (ego.W / 2.0 + 0.2):
                        return False  # Có xe ở sườn bên phải!
                else:  # Lách sang trái (d dương hơn)
                    if -(ego.W / 2.0 + 0.2) <= d_rel <= (abs(lat_shift) + v.W / 2.0 + 0.4):
                        return False  # Có xe ở sườn bên trái!

            # 2. Quét theo tọa độ Frenet cho các xe cùng nhánh
            branch_ego = getattr(ego, 'heading_branch', ego.origin)
            branch_v = getattr(v, 'heading_branch', v.origin)
            if branch_v == branch_ego:
                s_v, d_v = self.get_frenet_coords(v)
                if abs(s_v - s_ego) < (ego.L / 2.0 + v.L / 2.0 + 2.5):
                    v_d_min = d_v - v.W / 2.0
                    v_d_max = d_v + v.W / 2.0
                    if not (v_d_max < d_sweep_min or v_d_min > d_sweep_max):
                        return False

        return True

    def handle_intersection_ttc2d_and_swerving(self, ego, vehicles, dt=0.1):
        """
        Mô hình TTC 2D & Lách động học áp dụng cho dòng xe hỗn hợp (Multi-traffic):
        - CHỈ lách khi đã vượt qua vạch dừng đèn xanh đèn đỏ (s_ego >= -10.5m).
        - Kiểm tra khe hở và an toàn hai bên sườn (Lateral Clearance).
        - Khi lách, chuyển sang làn thẳng hợp lệ gần nhất (Lane 2: -5.25, Lane 3: -8.75).
        - Sau khi lách, giữ nguyên làn mới đã chuyển (không quay lại làn xuất phát).
        - Hysteresis: duy trì hướng lách đã cam kết cho tới khi vượt qua chướng ngại vật.
        """
        if ego.v_type != 'Motorcycle' or ego.turn_direction != 'Straight':
            return False

        s_ego, d_ego = self.get_frenet_coords(ego)

        # TUYỆT ĐỐI KHÔNG LÁCH KHI CHƯA QUA VẠCH DỪNG ĐÈN XANH ĐÈN ĐỎ
        if s_ego < -10.5:
            return False

        # ── Hysteresis: nếu đang lách, tiếp tục bám theo làn đã chọn cho tới khi vượt qua ──
        if getattr(ego, 'is_swerving', False) and getattr(ego, 'swerve_partner', None) is not None:
            partner = ego.swerve_partner
            p_nav = getattr(partner, 'nav_state', 'departed')

            # Khoảng cách dọc so với partner
            nose_x = partner.x + (partner.L / 2.0) * math.cos(partner.theta)
            nose_y = partner.y + (partner.L / 2.0) * math.sin(partner.theta)
            if ego.origin == 'North':
                dy = (-nose_y) - s_ego
            elif ego.origin == 'South':
                dy = nose_y - s_ego
            elif ego.origin == 'East':
                dy = (-nose_x) - s_ego
            else:
                dy = nose_x - s_ego

            # Hết xung đột: partner đã thoát ngã tư hoặc xe máy đã lách qua hẳn (dy < -1.5m)
            if p_nav in ['leaving', 'departed'] or dy < -1.5:
                # KẾT THÚC LÁCH: CẬP NHẬT LÀN ĐƯỜNG ĐÃ LÁCH SANG (KHÔNG QUAY VỀ LÀN CŨ!)
                committed_d = getattr(ego, 'committed_target_d', ego.target_d)
                ego.target_d = committed_d
                ego._exit_lane = abs(committed_d)
                ego.is_swerving = False
                ego.swerve_partner = None
                ego.active_ttc = None
                ego.committed_target_d = None
                return False

            # Vẫn đang trong xung đột → tiếp tục điều khiển xe bám theo committed_target_d
            committed_d = getattr(ego, 'committed_target_d', ego.target_d)
            ego.v_max_override = 3.5
            partner.v_max_override = self.LEFT_TURN_CREEP_SPEED
            self.apply_frenet_offset(ego, target_d=committed_d, K_p=0.4, dt=dt)
            return True

        opp_origin = {'North': 'South', 'South': 'North',
                      'East': 'West', 'West': 'East'}.get(ego.origin)
        if not opp_origin:
            return False

        critical_v = None
        min_ttc = float('inf')

        for v in vehicles:
            if v == ego or v.origin != opp_origin or v.turn_direction != 'Left':
                continue
            v_nav = getattr(v, 'nav_state', 'approaching')
            if v_nav not in ['approaching', 'in_intersection']:
                continue

            nose_x = v.x + (v.L / 2.0) * math.cos(v.theta)
            nose_y = v.y + (v.L / 2.0) * math.sin(v.theta)

            if ego.origin == 'North':
                s_nose = -nose_y
                d_nose = nose_x
            elif ego.origin == 'South':
                s_nose = nose_y
                d_nose = -nose_x
            elif ego.origin == 'East':
                s_nose = -nose_x
                d_nose = -nose_y
            else:
                s_nose = nose_x
                d_nose = nose_y

            # Điều kiện lấn làn: Mũi xe v chạm hoặc vượt qua tim đường vào làn thẳng (d_nose < 0.2)
            if d_nose < 0.2:
                dy = s_nose - s_ego
                if -1.5 < dy < 18.0:
                    v_closing = ego.v + max(0.0, -v.v * math.cos(v.theta - ego.theta))
                    ttc = dy / v_closing if (v_closing > 0.2 and dy > 0) else 99.0
                    if ttc < 4.5 and ttc < min_ttc:
                        min_ttc = ttc
                        critical_v = v

        if critical_v is not None:
            # Chọn làn thẳng thích hợp gần nhất để lách qua
            # Xe rẽ trái lấn từ tim đường (d >= -3.5m) sang phải
            # Nếu ego đang ở Lane 2 (d ~ -5.25), ưu tiên lách dạt sang Lane 3 (d = -8.75)
            # Nếu ego đang ở Lane 3 (d ~ -8.75), giữ Lane 3 (làn ngoài cùng an toàn nhất)
            target_lane = -8.75 if abs(d_ego) < 7.0 else -8.75

            if self.is_lateral_gap_clear(ego, target_lane, vehicles):
                ego.is_swerving = True
                ego.swerve_partner = critical_v
                ego.active_ttc = min_ttc
                ego.committed_target_d = target_lane
                # CẬP NHẬT TRỰC TIẾP TARGET_D SANG LÀN MỚI
                ego.target_d = target_lane
                ego._exit_lane = abs(target_lane)
                ego.v_max_override = 3.5
                critical_v.v_max_override = self.LEFT_TURN_CREEP_SPEED

                self.apply_frenet_offset(ego, target_d=target_lane, K_p=0.4, dt=dt)
                return True
            else:
                # Làn bên cạnh đang bị xe khác chiếm -> không lách, phanh giảm tốc nhường đường
                ego.is_swerving = False
                ego.v_max_override = 2.0
                critical_v.v_max_override = self.LEFT_TURN_CREEP_SPEED
                return False

        if getattr(ego, 'is_swerving', False):
            committed_d = getattr(ego, 'committed_target_d', ego.target_d)
            ego.target_d = committed_d
            ego._exit_lane = abs(committed_d)
            ego.is_swerving = False
            ego.swerve_partner = None
            ego.active_ttc = None
            ego.committed_target_d = None

        return False

    def get_bezier_points(self, veh):
        """
        Tính 3 điểm điều khiển Bezier bậc 2 cho quỹ đạo rẽ.

        P0 = vị trí thực của xe tại biên ngã tư (dùng tọa độ thực, không hardcode làn).
        P2 = điểm thoát ngã tư ở nhánh đích (làn phù hợp với hướng rẽ).
        P1 = giao điểm của hướng P0 và hướng P2 → tạo cung cua tự nhiên.
        """
        origin = veh.origin
        dest = veh.destination
        half_W = 10.5   # Bán chiều rộng ngã tư (10.5m)

        # ── P0: vị trí xe khi chạm biên ngã tư ──────────────────────────────
        if origin == 'West':
            P0 = (-half_W, veh.y)
        elif origin == 'East':
            P0 = (half_W, veh.y)
        elif origin == 'South':
            P0 = (veh.x, -half_W)
        else:  # North
            P0 = (veh.x, half_W)

        # ── P2: điểm ra tại làn đích ─────────────────────────────────────────
        # Rẽ trái → làn trong (1.75m), Rẽ phải → làn ngoài (8.75m), Đi thẳng → giữ làn
        if veh.turn_direction == 'Left':
            exit_lane = abs(getattr(veh, 'target_d', -1.75))
            if exit_lane > 5.25: exit_lane = 5.25 # Không cho xe rẽ trái dạt ra làn ngoài cùng
        elif veh.turn_direction == 'Right':
            exit_lane = abs(getattr(veh, 'target_d', -8.75))
            if exit_lane < 5.25: exit_lane = 5.25 # Không cho xe rẽ phải kẹp vào làn sát tim
        else: # Straight
            exit_lane = abs(getattr(veh, 'target_d', -5.25))
        # Mỗi hướng đến: xe chiếm phần đường BÊN PHẢI của nhánh đó
        #   East-bound → y âm (phía Nam), West-bound → y dương (phía Bắc)
        #   North-bound → x dương (phía Đông), South-bound → x âm (phía Tây)
        if dest == 'East':
            P2 = (half_W, -exit_lane)
        elif dest == 'West':
            P2 = (-half_W, exit_lane)
        elif dest == 'North':
            P2 = (exit_lane, half_W)
        else:  # South
            P2 = (-exit_lane, -half_W)

        # ── P1: góc cua (giao điểm tiếp tuyến tại P0 và P2) ─────────────────
        if origin in ['West', 'East']:
            P1 = (P2[0], P0[1])
        else:
            P1 = (P0[0], P2[1])

        # Lưu exit_lane để cập nhật target_d sau khi rẽ xong
        veh._exit_lane = exit_lane
        return P0, P1, P2

    def update_nav_state(self, veh):
        """
        Cập nhật trạng thái điều hướng khi vào ngã tư.
        """
        if not hasattr(veh, 'nav_state'):
            veh.nav_state = 'approaching'
            veh.heading_branch = veh.origin

        in_intersection = (abs(veh.x) <= 10.5 and abs(veh.y) <= 10.5)

        if veh.nav_state == 'approaching':
            if in_intersection:
                veh.nav_state = 'in_intersection'

        if veh.nav_state == 'in_intersection':
            just_left = False
            if veh.turn_direction == 'Straight':
                dist_from_center = math.hypot(veh.x, veh.y)
                if dist_from_center > 11.5:
                    if veh.destination == 'East' and veh.x > 10.5:
                        just_left = True
                    elif veh.destination == 'West' and veh.x < -10.5:
                        just_left = True
                    elif veh.destination == 'North' and veh.y > 10.5:
                        just_left = True
                    elif veh.destination == 'South' and veh.y < -10.5:
                        just_left = True
            else:
                if not hasattr(veh, 'turn_t'):
                    veh.turn_t = 0.0
                    veh.P0, veh.P1, veh.P2 = self.get_bezier_points(veh)
                    L_curve = math.hypot(veh.P0[0]-veh.P1[0], veh.P0[1]-veh.P1[1]) + math.hypot(
                        veh.P1[0]-veh.P2[0], veh.P1[1]-veh.P2[1])
                    veh.turn_length = max(L_curve * 0.75, 1.0)

                if veh.turn_t >= 1.0:
                    just_left = True
            
            if just_left:
                veh.nav_state = 'leaving'
                equiv_origin = {'East': 'West', 'West': 'East',
                                'North': 'South', 'South': 'North'}
                new_branch = equiv_origin[veh.destination]
                if veh.heading_branch != new_branch:
                    veh.heading_branch = new_branch
                    if veh.turn_direction == 'Straight':
                        # Tìm làn thẳng hợp lệ gần nhất với vị trí thực tế của xe
                        _, current_d = self.get_frenet_coords(veh)
                        valid_straight_lanes = [-1.75, -5.25, -8.75]
                        nearest_lane = min(valid_straight_lanes, key=lambda l: abs(current_d - l))
                        veh.target_d = nearest_lane
                        veh._exit_lane = abs(nearest_lane)
                    else:
                        exit_lane = getattr(veh, '_exit_lane', 1.75)
                        veh.target_d = -exit_lane

        if veh.nav_state == 'leaving':
            tail_x = veh.x - (veh.L/2) * math.cos(veh.theta)
            tail_y = veh.y - (veh.L/2) * math.sin(veh.theta)
            clear_margin = 11.5
            is_clear = False
            if veh.destination == 'East': is_clear = tail_x > clear_margin
            elif veh.destination == 'West': is_clear = tail_x < -clear_margin
            elif veh.destination == 'North': is_clear = tail_y > clear_margin
            elif veh.destination == 'South': is_clear = tail_y < -clear_margin
            
            if is_clear:
                veh.nav_state = 'departed'

    def update_steering(self, veh, dt):
        """
        Cập nhật góc lái theta theo đường cong Bezier.
        """
        if veh.nav_state == 'in_intersection' and veh.turn_direction != 'Straight':
            if not hasattr(veh, 'turn_length'):
                return
            veh.turn_t += (veh.v * dt) / veh.turn_length
            if veh.turn_t < 1.0:
                t_ahead = min(veh.turn_t + 2.0 / veh.turn_length, 1.0)
                t = t_ahead
                P_target_x = (
                    1-t)**2 * veh.P0[0] + 2*(1-t)*t * veh.P1[0] + t**2 * veh.P2[0]
                P_target_y = (
                    1-t)**2 * veh.P0[1] + 2*(1-t)*t * veh.P1[1] + t**2 * veh.P2[1]

                desired_theta = math.atan2(
                    P_target_y - veh.y, P_target_x - veh.x)
                diff = (desired_theta - veh.theta +
                        math.pi) % (2 * math.pi) - math.pi

                max_steer = math.radians(15)
                veh.theta += max(-max_steer, min(diff, max_steer))

    def step(self, vehicles, dt, signal_controller=None):
        active_ids = {id(v) for v in vehicles if getattr(v, 'nav_state', '') not in ['leaving', 'departed']}
        keys_to_del = [k for k in self.conflict_negotiations if k[0] not in active_ids or k[1] not in active_ids]
        for k in keys_to_del:
            del self.conflict_negotiations[k]

        for veh in vehicles:
            if not hasattr(veh, 'aggressiveness'):
                veh.aggressiveness = random.uniform(0.85, 1.25)
                base_spd = self.BASE_CONFLICT_SPEED_MOTO if veh.v_type == 'Motorcycle' else self.BASE_CONFLICT_SPEED_CAR
                veh.desired_conflict_speed = base_spd * veh.aggressiveness

        cz_vehicles = []
        for v in vehicles:
            if getattr(v, 'nav_state', '') in ['leaving', 'departed']:
                continue
            s_v, _ = self.get_frenet_coords(v)
            in_cz = (abs(v.x) <= self.CZ_HALF_SIZE and abs(v.y) <= self.CZ_HALF_SIZE) or getattr(v, 'nav_state', '') == 'in_intersection' or s_v >= -12.0
            if in_cz:
                cz_vehicles.append(v)

        n_cz = len(cz_vehicles)
        if n_cz <= 1: crowd_factor = 1.0
        elif n_cz == 2: crowd_factor = 0.90
        elif n_cz == 3: crowd_factor = 0.80
        elif n_cz == 4: crowd_factor = 0.72
        else: crowd_factor = max(0.65, 0.72 - 0.05 * (n_cz - 4))

        for v in cz_vehicles:
            target_cz_spd = v.desired_conflict_speed * crowd_factor
            if n_cz <= 1 and v.turn_direction == 'Straight':
                target_cz_spd = min(v.v_max, 6.5)
            v.cz_speed_cap = target_cz_spd

        for veh in vehicles:
            self.update_nav_state(veh)
            lead_veh = self.get_lead_vehicle(veh, vehicles)
            s_ego, d_ego = self.get_frenet_coords(veh)

            if getattr(veh, 'cz_speed_cap', None) is not None and getattr(veh, 'nav_state', '') in ['approaching', 'in_intersection']:
                if s_ego >= -15.0:
                    curr_cap = veh.v_max if getattr(veh, 'v_max_override', None) is None else veh.v_max_override
                    veh.v_max_override = min(curr_cap, veh.cz_speed_cap)

            conflict_veh = self.get_conflict_vehicle(veh, vehicles, signal_controller)
            if conflict_veh is not None:
                if lead_veh is None or self.get_frenet_coords(lead_veh)[0] > conflict_veh.s:
                    lead_veh = conflict_veh

            defensive_veh = self.get_defensive_lead(veh, vehicles, signal_controller)
            if defensive_veh is not None:
                if lead_veh is None or self.get_frenet_coords(lead_veh)[0] > defensive_veh.s:
                    lead_veh = defensive_veh

            # Signal
            if signal_controller:
                state = signal_controller.get_state(veh.origin)
                front_s = s_ego + veh.L / 2.0
                dist_to_stop = -10.5 - front_s

                if state == 'R':
                    veh.dilemma_decision = None
                    if dist_to_stop > 0.0:
                        dummy = DummyVehicle(s=-10.5)
                        if lead_veh is None or (self.get_frenet_coords(lead_veh)[0] - lead_veh.L/2 > -10.5):
                            lead_veh = dummy
                elif state == 'Y':
                    if dist_to_stop > 0.0:
                        tti = dist_to_stop / veh.v if veh.v > 0.5 else 999.0
                        if veh.dilemma_decision is None:
                            if tti > 5.0: veh.dilemma_decision = 'Stop'
                            elif tti < 1.5: veh.dilemma_decision = 'Go'
                            else:
                                p_stop = 1.0 / (1.0 + math.exp(5.816 - 1.620 * tti))
                                veh.dilemma_decision = 'Stop' if random.random() < p_stop else 'Go'

                        if veh.dilemma_decision == 'Stop':
                            dummy = DummyVehicle(s=-10.5)
                            if lead_veh is None or (self.get_frenet_coords(lead_veh)[0] - lead_veh.L/2 > -10.5):
                                lead_veh = dummy
                elif state == 'G':
                    veh.dilemma_decision = None

            # Straight vs Left yielding hold lines
            opp_origin = {'North': 'South', 'South': 'North',
                          'East': 'West', 'West': 'East'}.get(veh.origin)
            front_s = s_ego + veh.L / 2.0

            if veh.turn_direction == 'Straight' and veh.nav_state in ['approaching', 'in_intersection']:
                active_opp_left = None
                for v in vehicles:
                    if (v.origin == opp_origin and v.turn_direction == 'Left'
                            and getattr(v, 'nav_state', 'approaching') in ['approaching', 'in_intersection']):
                        s_v, _ = self.get_frenet_coords(v)
                        turn_p = getattr(v, 'turn_t', 0.0)
                        is_cleared = (turn_p >= 0.98 or getattr(v, 'nav_state', '') in ['leaving', 'departed'])
                        is_inactive = (s_v < -10.0 and v.v < 0.5)
                        if -12.0 <= s_v <= 10.0 and not is_cleared and not is_inactive:
                            winner, yielder = self.resolve_head_to_head_conflict(veh, v)
                            if veh == yielder:
                                active_opp_left = v
                                break

                if active_opp_left is not None:
                    dist_to_center = 0.0 - s_ego
                    if -3.0 < dist_to_center < 25.0:
                        wait_too_long = getattr(veh, 'yield_wait_time', 0.0) > 2.5
                        if not wait_too_long:
                            veh.yield_wait_time = getattr(veh, 'yield_wait_time', 0.0) + dt
                            if front_s < self.STRAIGHT_WAIT_S:
                                veh.v_max_override = self.STRAIGHT_YIELD_SPEED
                                wait_dummy = DummyVehicle(s=self.STRAIGHT_WAIT_S, v=0.0)
                            else:
                                wait_dummy = DummyVehicle(s=s_ego + 0.4, v=0.0)
                            if lead_veh is None or self.get_frenet_coords(lead_veh)[0] > wait_dummy.s:
                                lead_veh = wait_dummy
                        else:
                            veh.v_max_override = 2.5
                else:
                    veh.yield_wait_time = max(0.0, getattr(veh, 'yield_wait_time', 0.0) - dt * 0.5)

            elif veh.turn_direction == 'Left' and veh.nav_state in ['approaching', 'in_intersection']:
                threatening_straight = None
                for v in vehicles:
                    if (v.origin == opp_origin and v.turn_direction == 'Straight'
                            and getattr(v, 'nav_state', 'approaching') in ['approaching', 'in_intersection']):
                        s_v, _ = self.get_frenet_coords(v)
                        if -15.0 <= s_v <= 5.0:
                            winner, yielder = self.resolve_head_to_head_conflict(v, veh)
                            if veh == yielder:
                                threatening_straight = v
                                break

                if threatening_straight is not None:
                    if getattr(veh, 'turn_t', 0.0) > 0.75:
                        veh.v_max_override = 4.0
                    else:
                        s_threat, _ = self.get_frenet_coords(threatening_straight)
                        threat_in_zone = (-3.5 <= s_threat <= 3.5 and threatening_straight.v > 0.5)
                        wait_too_long = getattr(veh, 'yield_wait_time', 0.0) > 2.5 and not threat_in_zone
                        if not wait_too_long:
                            veh.yield_wait_time = getattr(veh, 'yield_wait_time', 0.0) + dt
                            if front_s < self.LEFT_TURN_WAIT_S:
                                if front_s < self.LEFT_TURN_WAIT_S - 2.0:
                                    veh.v_max_override = self.LEFT_TURN_CREEP_SPEED
                                    wait_dummy = None
                                else:
                                    wait_dummy = DummyVehicle(s=self.LEFT_TURN_WAIT_S, v=0.0)
                            else:
                                wait_dummy = DummyVehicle(s=s_ego + 0.4, v=0.0)
                            if wait_dummy is not None:
                                if lead_veh is None or self.get_frenet_coords(lead_veh)[0] > wait_dummy.s:
                                    lead_veh = wait_dummy
                        else:
                            veh.v_max_override = 2.5
                else:
                    veh.yield_wait_time = max(0.0, getattr(veh, 'yield_wait_time', 0.0) - dt * 0.5)
                    veh.v_max_override = 4.0

            v0_orig = veh.v_max
            if getattr(veh, 'v_max_override', None) is not None:
                veh.v_max = min(veh.v_max, veh.v_max_override)
                veh.v_max_override = None

            a_target = self.compute_idm(veh, lead_veh)

            if veh.turn_direction != 'Straight':
                R_c = 8.0 if veh.turn_direction == 'Left' else 1.75
                a_lat = 2.0
                v_turn_des = math.sqrt(a_lat * R_c)
                v_turn_des = min(v_turn_des, veh.v_max)

                if veh.nav_state == 'approaching':
                    D_decel = max(0.0, (veh.v**2 - v_turn_des ** 2) / (2 * abs(veh.a_comf)))
                    dist_to_stop = -10.0 - s_ego
                    if dist_to_stop <= D_decel:
                        a_target = min(a_target, veh.a_comf)
                elif veh.nav_state == 'in_intersection':
                    if veh.v > v_turn_des:
                        a_target = min(a_target, veh.a_comf)

            if veh.v_type == 'Motorcycle' and veh.nav_state in ['approaching', 'in_intersection']:
                if s_ego >= -10.5:
                    swerved = self.compute_lateral_swerving(veh, lead_veh, dt) if lead_veh else False
                    if not swerved:
                        self.apply_frenet_offset(veh, veh.target_d, K_p=0.35, dt=dt)
                else:
                    self.apply_frenet_offset(veh, veh.target_d, K_p=0.35, dt=dt)
            elif veh.turn_direction == 'Straight' or veh.nav_state in ['leaving', 'departed']:
                self.apply_frenet_offset(veh, veh.target_d, K_p=0.35, dt=dt)

            veh.v_max = v0_orig
            veh.set_acceleration(a_target)
            self.update_steering(veh, dt)

        for veh in vehicles:
            veh.update_state(dt)

