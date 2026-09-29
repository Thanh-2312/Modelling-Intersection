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

        # Vị trí xa nhất xe rẽ trái được phép nhích vào khi chờ khe hở (Mục 4.3)
        self.LEFT_TURN_WAIT_S = -1.0
        # Ngưỡng vận tốc (m/s): xe rẽ trái đi chậm hơn mức này → đang chờ khe hở
        self.LEFT_TURN_BLOCK_SPEED = 2.0

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

    def apply_frenet_offset(self, veh, target_d=None, K_p=0.2):
        """
        Thay đổi góc lái theta để đưa phương tiện về tọa độ ngang target_d.
        Chỉ dùng khi đi thẳng hoặc đã rẽ xong.
        """
        if target_d is None:
            target_d = getattr(veh, 'target_d', -1.75)
        _, current_d = self.get_frenet_coords(veh)
        error_d = target_d - current_d

        steer_angle = error_d * K_p

        max_steer = math.radians(15)
        steer_angle = max(-max_steer, min(steer_angle, max_steer))

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

        veh.theta = base_theta + steer_angle

    def compute_idm(self, ego, lead):
        v = ego.v
        v0 = ego.v_max
        a_max = ego.a_max
        b = abs(ego.a_comf)

        if lead is None:
            return a_max * (1 - (v / v0)**self.delta)

        s_ego, _ = self.get_frenet_coords(ego)
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

        for v in vehicles:
            if v == ego:
                continue
            branch_v = getattr(v, 'heading_branch', v.origin)
            if branch_v != branch_ego:
                continue

            s_v, d_v = self.get_frenet_coords(v)
            if s_v > s_ego:
                s_gap = s_v - s_ego
                if abs(d_v - d_ego) < (v.W/2 + ego.W/2 + 0.1):
                    if s_gap < min_s_gap:
                        min_s_gap = s_gap
                        lead_veh = v

        return lead_veh

    def paths_conflict(self, v1, v2):
        if v1.origin == v2.origin:
            return False
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
            return True
        if v1.turn_direction == 'Right' and v2.turn_direction == 'Right':
            return False
        return True

    def get_conflict_vehicle(self, ego, vehicles, signal_controller=None):
        """
        Xử lý xung đột quyền ưu tiên tại ngã tư (Intersection Priority & Conflict Avoidance).
        Ngăn chặn Deadlock và đảm bảo tuân thủ luật giao thông:
        1. Phương tiện đã vào ngã tư ('in_intersection') được ưu tiên giải phóng ngã tư, 
           không nhường xe còn ở ngoài ('approaching').
        2. Xe đi thẳng có quyền ưu tiên cao hơn xe rẽ.
        3. Xe không nhường xe đang dừng chờ đèn đỏ.
        4. Tránh Deadlock khi vận tốc nhỏ bằng cách so sánh vị trí thực tế tới tâm và dùng v_eff.
        """
        if getattr(ego, 'nav_state', '') in ['leaving', 'departed']:
            return None

        dist_ego = math.hypot(ego.x, ego.y)
        if dist_ego > 15.0:
            return None

        # Vận tốc hiệu dụng để ước tính thời gian, tránh chia cho 0 hoặc v quá nhỏ gây Deadlock
        v_ego_eff = max(ego.v, 3.0)
        t_ego = dist_ego / v_ego_eff
        s_ego, _ = self.get_frenet_coords(ego)

        conflict_dummy = None
        min_t_ego = float('inf')

        # Hàm tính điểm ưu tiên theo công thức AI.md mục 4.4:
        # Score = -1.0*TTI + 1.5*I_straight + 0.5*I_right + 2.0*I_intersection
        # Xe có điểm số THẤP HƠN phải nhường
        def priority_score(veh, dist, v_eff):
            TTI = dist / v_eff
            I_straight = 1.5 if veh.turn_direction == 'Straight' else 0.0
            I_right = 0.5 if veh.turn_direction == 'Right' else 0.0
            I_intersection = 2.0 if getattr(veh, 'nav_state', '') == 'in_intersection' else 0.0
            return -1.0 * TTI + I_straight + I_right + I_intersection

        for v in vehicles:
            if v == ego or getattr(v, 'nav_state', '') in ['leaving', 'departed']:
                continue
            dist_v = math.hypot(v.x, v.y)
            if dist_v > 15.0:
                continue

            v_nav = getattr(v, 'nav_state', 'approaching')

            # 1. Xe đã vào ngã tư có quyền ưu tiên giải phóng ngã tư trước xe chưa vào
            if ego.nav_state == 'in_intersection' and v_nav == 'approaching':
                continue

            # 2. Không nhường xe đang bị đèn đỏ chặn ở vạch dừng
            if signal_controller and v_nav == 'approaching':
                if signal_controller.get_state(v.origin) == 'R':
                    continue

            # 3. Kiểm tra xem 2 quỹ đạo có giao cắt không
            if not self.paths_conflict(ego, v):
                continue

            # 4. Xung đột giữa 2 xe ngược chiều:
            # Xe đi thẳng ưu tiên tuyệt đối; rẽ trái đã có Gap Acceptance
            opp_origin = {'North': 'South', 'South': 'North',
                          'East': 'West', 'West': 'East'}.get(ego.origin)
            if v.origin == opp_origin:
                if ego.turn_direction == 'Straight':
                    continue
                elif ego.turn_direction == 'Left' and v.turn_direction == 'Straight':
                    continue

            # 5. Phân định quyền ưu tiên bằng công thức điểm số (Mục 4.4 AI.md)
            v_v_eff = max(v.v, 3.0)
            score_ego = priority_score(ego, dist_ego, v_ego_eff)
            score_v = priority_score(v, dist_v, v_v_eff)

            ego_yields = (score_ego < score_v)

            if ego_yields:
                # Nếu ego đang ở ngoài tiếp cận, dừng trước vạch dừng hoặc mép ngã tư
                # Nếu ego đã lỡ vào ngã tư, không dừng chết mà cho nhích từ từ (v = 1.0 m/s)
                if ego.nav_state == 'in_intersection':
                    yield_s = s_ego + 1.0
                    dummy = DummyVehicle(s=yield_s, v=1.0)
                else:
                    yield_s = min(s_ego + 0.5, -10.5)
                    dummy = DummyVehicle(s=yield_s, v=0.0)

                if t_ego < min_t_ego:
                    min_t_ego = t_ego
                    conflict_dummy = dummy

        return conflict_dummy

    def get_defensive_lead(self, ego, vehicles):
        """
        Phanh phòng thủ 2D (Defensive Collision Avoidance / AEB).
        Quét hành lang an toàn 2D phía trước mũi xe ego. Nếu có bất kỳ xe nào (kể cả xe ngược chiều
        đang chờ rẽ trái, xe đang thoát ngã tư, hoặc đuôi xe đang ôm cua) chắn ngang đường,
        tự động trả về xe ảo để mô hình IDM phanh dừng an toàn, không bao giờ đâm xuyên.
        """
        closest_gap = float('inf')
        defensive_dummy = None

        cos_ego = math.cos(ego.theta)
        sin_ego = math.sin(ego.theta)
        s_ego, _ = self.get_frenet_coords(ego)

        for v in vehicles:
            if v == ego:
                continue

            dx = v.x - ego.x
            dy = v.y - ego.y

            # Tọa độ tương đối trong hệ trục cục bộ của ego (Forward / Lateral)
            s_rel = dx * cos_ego + dy * sin_ego
            d_rel = -dx * sin_ego + dy * cos_ego

            # Chỉ quét phía trước trong phạm vi an toàn (tối đa 25m)
            # Bắt đầu từ 0.2m phía trước tâm xe để không bắt các xe phía sau
            if s_rel <= 0.2 or s_rel > 25.0:
                continue

            delta_theta = v.theta - ego.theta
            abs_cos = abs(math.cos(delta_theta))
            abs_sin = abs(math.sin(delta_theta))

            # Kích thước hình chiếu của xe v lên hệ trục của ego
            L_v_proj = v.L * abs_cos + v.W * abs_sin
            W_v_proj = v.L * abs_sin + v.W * abs_cos

            # Bề rộng hành lang an toàn theo AI.md mục 4.5.1 Bước 3:
            # margin = -0.2m cho xe máy (cho phép khai thác khe hẹp)
            # margin = 0.0m cho ô tô
            margin = -0.2 if ego.v_type == 'Motorcycle' else 0.0
            corridor_half_width = (ego.W + W_v_proj) / 2.0 + margin

            if abs(d_rel) < corridor_half_width:
                # Tính khoảng cách thông thủy giữa đầu ego và đuôi v
                gap = s_rel - (L_v_proj / 2.0) - (ego.L / 2.0)
                if gap < closest_gap:
                    closest_gap = gap
                    # Vận tốc chiếu dọc theo hướng tiến của ego
                    v_longitudinal = max(0.0, v.v * math.cos(delta_theta))

                    dummy_s = s_ego + s_rel
                    _, d_v = self.get_frenet_coords(v)
                    dummy = DummyVehicle(s=dummy_s, d=d_v, v=v_longitudinal)
                    dummy.L = L_v_proj
                    dummy.W = v.W
                    dummy.v_type = v.v_type
                    defensive_dummy = dummy

        return defensive_dummy

    def compute_lateral_swerving(self, ego_moto, lead_car):
        """
        Lách ngang cho xe máy. Trả về True nếu xe máy ĐÃ LÁCH THÀNH CÔNG (đã thoát hẳn khỏi hình chiếu ngang của ô tô).
        """
        # Tuyệt đối không lách xe ảo (DummyVehicle đại diện cho chướng ngại vật/vạch dừng)
        if getattr(lead_car, 'is_dummy', False):
            return False

        s_ego, d_ego = self.get_frenet_coords(ego_moto)
        s_lead, d_lead = self.get_frenet_coords(lead_car)
        s_gap = (s_lead - lead_car.L/2) - (s_ego + ego_moto.L/2)

        # Nếu khoảng cách quá xa (> 30m) hoặc xe máy đã vượt qua đầu xe ô tô
        if s_gap > 30.0 or s_gap < -0.5:
            return False

        # Không cho phép lách khi đang ở khu vực vạch dừng hoặc tiếp cận ngã tư (-15m đến 5m)
        # Giúp loại bỏ hoàn toàn hành vi xe máy đâm xuyên ô tô khi dừng chờ và khi đèn xanh vừa bật
        if -15.0 <= s_ego <= 5.0:
            return False

        # Ranh giới làn đường đi (chỉ đi bên phải tâm đường: 1 làn rộng 3.5m)
        d_left_bound = 0.0   # Tâm đường
        d_right_bound = -3.5  # Lề phải / vỉa hè (3.5m)

        car_left_edge = d_lead + lead_car.W/2
        car_right_edge = d_lead - lead_car.W/2

        gap_left = d_left_bound - car_left_edge
        gap_right = car_right_edge - d_right_bound
        req_gap = ego_moto.W + 0.4  # Cần tối thiểu 1.2m khoảng trống
        target_d = None

        if gap_left >= req_gap and gap_right >= req_gap:
            if gap_left >= gap_right:
                target_d = car_left_edge + req_gap/2
            else:
                target_d = car_right_edge - req_gap/2
        elif gap_left >= req_gap:
            target_d = car_left_edge + req_gap/2
        elif gap_right >= req_gap:
            target_d = car_right_edge - req_gap/2

        if target_d is not None:
            # Giới hạn target_d an toàn, tránh xe máy lách tràn ra ngoài mép đường hoặc đè qua tim đường
            min_d = d_right_bound + ego_moto.W / 2 + 0.1
            max_d = d_left_bound - ego_moto.W / 2 - 0.1
            target_d = max(min_d, min(target_d, max_d))
            self.apply_frenet_offset(ego_moto, target_d)

            # CHỈ coi là lách thành công (cho phép vượt) khi thân xe máy THỰC TẾ ĐÃ TÁCH RỜI HẲN khỏi ô tô theo phương ngang
            lateral_clearance = abs(d_ego - d_lead) - \
                (ego_moto.W/2 + lead_car.W/2)
            if lateral_clearance >= 0.15:
                return True
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

    def update_navigation(self, veh, dt):
        """
        Điều hướng rẽ khi vào ngã tư.
        """
        if not hasattr(veh, 'nav_state'):
            veh.nav_state = 'approaching'
            veh.heading_branch = veh.origin

        in_intersection = (abs(veh.x) <= 11.5 and abs(veh.y) <= 11.5)

        if veh.nav_state == 'approaching':
            if in_intersection:
                veh.nav_state = 'in_intersection'

        if veh.nav_state == 'in_intersection':
            if veh.turn_direction == 'Straight':
                dist_from_center = math.hypot(veh.x, veh.y)
                if dist_from_center > 11.5:
                    if veh.destination == 'East' and veh.x > 10.5:
                        veh.nav_state = 'leaving'
                    elif veh.destination == 'West' and veh.x < -10.5:
                        veh.nav_state = 'leaving'
                    elif veh.destination == 'North' and veh.y > 10.5:
                        veh.nav_state = 'leaving'
                    elif veh.destination == 'South' and veh.y < -10.5:
                        veh.nav_state = 'leaving'
            else:
                if not hasattr(veh, 'turn_t'):
                    veh.turn_t = 0.0
                    veh.P0, veh.P1, veh.P2 = self.get_bezier_points(veh)
                    L_curve = math.hypot(veh.P0[0]-veh.P1[0], veh.P0[1]-veh.P1[1]) + math.hypot(
                        veh.P1[0]-veh.P2[0], veh.P1[1]-veh.P2[1])
                    veh.turn_length = max(L_curve * 0.75, 1.0)

                veh.turn_t += (veh.v * dt) / veh.turn_length
                if veh.turn_t >= 1.0:
                    veh.nav_state = 'leaving'
                else:
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

        if veh.nav_state == 'leaving':
            equiv_origin = {'East': 'West', 'West': 'East',
                            'North': 'South', 'South': 'North'}
            new_branch = equiv_origin[veh.destination]
            if veh.heading_branch != new_branch:
                veh.heading_branch = new_branch
                # Cập nhật target_d sang hệ toạ độ nhánh mới sau khi rẽ xong
                exit_lane = getattr(veh, '_exit_lane', 1.75)
                veh.target_d = -exit_lane
            veh.nav_state = 'departed'

    def step(self, vehicles, dt, signal_controller=None):
        for veh in vehicles:
            # 1. Điều hướng ngã tư (Chỉnh theta) bằng Bezier Curve
            self.update_navigation(veh, dt)

            # 2. Tìm xe phía trước
            lead_veh = self.get_lead_vehicle(veh, vehicles)

            s_ego, d_ego = self.get_frenet_coords(veh)

            # 2.1 Xử lý xung đột ngã tư chung (Intersection Conflict Avoidance)
            conflict_dummy = self.get_conflict_vehicle(
                veh, vehicles, signal_controller)
            if conflict_dummy is not None:
                if lead_veh is None or self.get_frenet_coords(lead_veh)[0] > conflict_dummy.s:
                    lead_veh = conflict_dummy

            # 2.2 Phanh phòng thủ 2D (Defensive Driving / Collision Corridor)
            # Quét chướng ngại vật thực tế chắn ngang hành lang 2D phía trước mũi xe (tránh đâm xuyên xe chờ/rẽ)
            defensive_dummy = self.get_defensive_lead(veh, vehicles)
            if defensive_dummy is not None:
                if lead_veh is None or self.get_frenet_coords(lead_veh)[0] > defensive_dummy.s:
                    lead_veh = defensive_dummy

            # 3. Swerving & Giữ làn
            if veh.nav_state != 'in_intersection':
                swerving = False
                if (veh.v_type == 'Motorcycle' and lead_veh is not None
                        and getattr(lead_veh, 'v_type', '') == 'Car'
                        and not getattr(lead_veh, 'is_dummy', False)):
                    swerving = self.compute_lateral_swerving(veh, lead_veh)
                    if swerving:
                        lead_veh = None
                if not swerving:
                    target_d = getattr(veh, 'target_d', -1.75)
                    self.apply_frenet_offset(veh, target_d=target_d)

            # 4. Đèn tín hiệu & Vùng lưỡng lự (chỉ áp dụng cho xe đang tiếp cận chưa qua vạch dừng)
            if signal_controller and veh.nav_state == 'approaching':
                state = signal_controller.get_state(veh.origin)
                front_s = s_ego + veh.L / 2
                dist_to_stop = -10.5 - front_s

                if state == 'R':
                    # Chỉ dừng nếu đầu xe chưa vượt qua vạch dừng (-10.5)
                    if dist_to_stop > 0.0:
                        dummy = DummyVehicle(s=-10.5)
                        if lead_veh is None or (self.get_frenet_coords(lead_veh)[0] - lead_veh.L/2 > -10.5):
                            lead_veh = dummy
                elif state == 'Y':
                    if dist_to_stop > 0.0:
                        tti = dist_to_stop / veh.v if veh.v > 0.5 else 999.0
                        if veh.dilemma_decision is None:
                            if tti > 5.0:
                                veh.dilemma_decision = 'Stop'
                            elif tti < 1.5:
                                veh.dilemma_decision = 'Go'
                            else:
                                p_stop = 1.0 / \
                                    (1.0 + math.exp(5.816 - 1.620 * tti))
                                veh.dilemma_decision = 'Stop' if random.random() < p_stop else 'Go'

                        if veh.dilemma_decision == 'Stop':
                            dummy = DummyVehicle(s=-10.5)
                            if lead_veh is None or (self.get_frenet_coords(lead_veh)[0] - lead_veh.L/2 > -10.5):
                                lead_veh = dummy
                elif state == 'G':
                    veh.dilemma_decision = None

            # 5. Gap Acceptance (Rẽ trái)
            if veh.turn_direction == 'Left' and veh.nav_state in ['approaching', 'in_intersection']:
                opp_origin = {'North': 'South', 'South': 'North',
                              'East': 'West', 'West': 'East'}.get(veh.origin)
                min_gap = 999.0
                for v in vehicles:
                    v_nav_state = getattr(v, 'nav_state', 'approaching')
                    if v.origin == opp_origin and v.turn_direction == 'Straight' and v_nav_state in ['approaching', 'in_intersection']:
                        s_v, _ = self.get_frenet_coords(v)
                        dist_to_center = 0.0 - s_v
                        if dist_to_center > -2.0:
                            gap = dist_to_center / v.v if v.v > 0.5 else 999.0
                            if gap < min_gap:
                                min_gap = gap

                crit_gap = 3.5 if veh.v_type == 'Car' else 3.0
                if min_gap < crit_gap:
                    # Không đủ khoảng trống an toàn: Dừng chờ an toàn trước khi cắt qua tim đường
                    yield_s = -10.5 if veh.nav_state == 'approaching' else min(
                        s_ego + 0.5, self.LEFT_TURN_WAIT_S)
                    # Nếu xe đã nhích chờ (vận tốc thấp), cho phép nhích chậm (v_creep = 1.0) thay vì v=0.0
                    v_dummy = 1.0 if veh.nav_state == 'in_intersection' else 0.0
                    dummy = DummyVehicle(s=yield_s, v=v_dummy)
                    if lead_veh is None or self.get_frenet_coords(lead_veh)[0] > yield_s:
                        lead_veh = dummy

            # 6. Tính IDM & Giảm tốc trước khi rẽ
            a_target = self.compute_idm(veh, lead_veh)

            if veh.turn_direction != 'Straight':
                R_c = 5.25 if veh.turn_direction == 'Left' else 1.75
                a_lat = 2.0
                v_turn_des = math.sqrt(a_lat * R_c)

                if veh.nav_state == 'approaching':
                    D_decel = max(0.0, (veh.v**2 - v_turn_des **
                                  2) / (2 * abs(veh.a_comf)))
                    dist_to_stop = -10.0 - s_ego
                    if 0 < dist_to_stop <= D_decel + 5.0 and veh.v > v_turn_des:
                        v0_orig = veh.v_max
                        veh.v_max = v_turn_des
                        a_decel = self.compute_idm(veh, lead_veh)
                        veh.v_max = v0_orig
                        a_target = min(a_target, a_decel)
                elif veh.nav_state == 'in_intersection':
                    if veh.v > v_turn_des:
                        v0_orig = veh.v_max
                        veh.v_max = v_turn_des
                        a_decel = self.compute_idm(veh, lead_veh)
                        veh.v_max = v0_orig
                        a_target = min(a_target, a_decel)

            veh.set_acceleration(a_target)

        # 5. Cập nhật vị trí
        for veh in vehicles:
            veh.update_state(dt)


# Khối Test nhanh
if __name__ == "__main__":
    controller = VehicleController()
    print("Control module compiled successfully!")
