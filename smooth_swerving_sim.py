"""
MÔ PHỎNG VI MÔ HÀNH VI LÁCH MƯỢT MÀ QUA ĐẦU XE TẠI NGÃ TƯ KHÔNG ĐÈN
====================================================================
Kịch bản:
- Xe Máy (Bắc -> Nam, Đi thẳng, Màu Xanh Dương): Tiếp cận từ phía Bắc.
- Ô Tô (Nam -> Tây, Rẽ trái, Màu Đỏ Cam): Tiếp cận từ phía Nam, rẽ trái sang phía Tây.
- Giao lộ KHÔNG có đèn tín hiệu và KHÔNG vẽ trước quỹ đạo.
- Khi Ô Tô rẽ trái và đầu mũi xe lấn qua trục dọc vào làn đi thẳng (x < 0):
  + Cả hai xe lập tức nhận diện nguy cơ va chạm và kích hoạt tín hiệu TTC.
  + Cả hai xe giảm tốc mượt mà bò chậm (KHÔNG DỪNG HẲN).
  + Xe Máy phản ứng động học (Dynamic Kinematic Steering) lách cong mượt mà sang phía Tây
    (đầu mũi xe máy nghiêng về phía Tây) để lách an toàn qua đầu Ô Tô.
  + Sau khi vượt qua mũi Ô Tô, xe máy trả lái về làn và cả hai xe cùng tăng tốc thoát giao lộ.
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
from matplotlib.widgets import Button
from matplotlib.animation import FuncAnimation

# ==============================================================================
# 1. CẤU HÌNH VẬT LÝ VÀ HÌNH HỌC (PHYSICAL & GEOMETRICAL CONFIGURATION)
# ==============================================================================
LANE_WIDTH = 3.50       # Chiều rộng 1 làn đường tiêu chuẩn (m)
NUM_LANES_PER_DIR = 2   # 2 làn vào + 2 làn ra mỗi nhánh (Tổng 4 làn = 14m)
HALF_ROAD = LANE_WIDTH * NUM_LANES_PER_DIR  # 7.0 m (từ tim đường đến mép vỉa hè)
TOTAL_ROAD_WIDTH = HALF_ROAD * 2            # 14.0 m

# Kích thước phương tiện
CAR_L = 4.60            # Chiều dài ô tô (m)
CAR_W = 1.80            # Chiều rộng ô tô (m)
MOTO_L = 2.00           # Chiều dài xe máy (m)
MOTO_W = 0.80           # Chiều rộng xe máy (m)
WHEELBASE_MOTO = 1.35   # Chiều dài cơ sở xe máy (m)

# Vận tốc mục tiêu (m/s)
V_CRUISE = 8.5          # Tốc độ chạy thông thường ~ 30.6 km/h
V_CREEP_1 = 3.3         # Tốc độ bò chậm Xe Máy ~ 11.9 km/h (KHÔNG DỪNG)
V_CREEP_2 = 2.0         # Tốc độ bò chậm Ô Tô ~ 7.2 km/h (KHÔNG DỪNG)
A_DECEL_MAX = -2.5      # Gia tốc giảm tốc tối đa êm ái (m/s^2)
A_ACCEL_MAX = 2.0       # Gia tốc tăng tốc (m/s^2)

# Giới hạn khung hình
VIEW_LIMIT = 26.0       # Phạm vi hiển thị đồ họa (m)
DT = 0.05               # Bước thời gian mô phỏng (s)

# ==============================================================================
# 2. QUỸ ĐẠO BÉZIER TỰ NHIÊN CHO XE RẼ TRÁI (SOUTH -> WEST)
# ==============================================================================
P0_LEFT = np.array([1.75, -HALF_ROAD])      # Điểm bắt đầu vào ngã tư
P1_LEFT = np.array([1.75, 1.75])            # Điểm điều khiển tiếp tuyến
P2_LEFT = np.array([-HALF_ROAD, 1.75])     # Điểm ra ngã tư hướng Tây

U_SAMPLES = np.linspace(0.0, 1.0, 600)
CURVE_PTS = np.array([(1 - u)**2 * P0_LEFT + 2 * (1 - u) * u * P1_LEFT + u**2 * P2_LEFT for u in U_SAMPLES])
CURVE_DIFFS = np.diff(CURVE_PTS, axis=0)
CURVE_SEGS = np.sqrt(np.sum(CURVE_DIFFS**2, axis=1))
S_CURVE = np.insert(np.cumsum(CURVE_SEGS), 0, 0.0)
L_TURN_CURVE = S_CURVE[-1]  # ~ 14.20 m

DIST_APPROACH_2 = 25.0  # Quãng đường tiếp cận từ vạch xuất phát
S_TOTAL_ROUTE_2 = DIST_APPROACH_2 + L_TURN_CURVE + 25.0


def get_car2_pose_at(s_traveled):
    """Tính vị trí (x, y) và góc hướng theta (rad) của Ô Tô rẽ trái theo quãng đường s."""
    if s_traveled <= DIST_APPROACH_2:
        x = 1.75
        y = -DIST_APPROACH_2 - HALF_ROAD + s_traveled
        theta = np.pi / 2.0
    elif s_traveled <= DIST_APPROACH_2 + L_TURN_CURVE:
        s_turn = s_traveled - DIST_APPROACH_2
        u = float(np.interp(s_turn, S_CURVE, U_SAMPLES))
        B = (1 - u)**2 * P0_LEFT + 2 * (1 - u) * u * P1_LEFT + u**2 * P2_LEFT
        dB = 2 * (1 - u) * (P1_LEFT - P0_LEFT) + 2 * u * (P2_LEFT - P1_LEFT)
        theta = math.atan2(dB[1], dB[0])
        x, y = float(B[0]), float(B[1])
    else:
        s_exit = s_traveled - (DIST_APPROACH_2 + L_TURN_CURVE)
        x = -HALF_ROAD - s_exit
        y = 1.75
        theta = np.pi
    return x, y, theta


def get_car_corners(x, y, theta, L, W):
    """Lấy tọa độ 4 đỉnh hình chữ nhật xe trong hệ tọa độ thế giới."""
    cos_t = math.cos(theta)
    sin_t = math.sin(theta)
    dx = L / 2.0
    dy = W / 2.0
    local_corners = np.array([
        [ dx,  dy],
        [ dx, -dy],
        [-dx, -dy],
        [-dx,  dy]
    ])
    R = np.array([[cos_t, -sin_t], [sin_t, cos_t]])
    return (R @ local_corners.T).T + np.array([x, y])


def compute_min_clearance(c1, c2):
    """Tính khoảng cách thông thủy nhỏ nhất giữa 2 xe (m)."""
    pts1, pts2 = [], []
    for i in range(4):
        for a in np.linspace(0, 1, 6):
            pts1.append((1 - a) * c1[i] + a * c1[(i + 1) % 4])
            pts2.append((1 - a) * c2[i] + a * c2[(i + 1) % 4])
    pts1 = np.array(pts1)
    pts2 = np.array(pts2)
    diffs = pts1[:, None, :] - pts2[None, :, :]
    dists = np.sqrt(np.sum(diffs**2, axis=-1))
    return float(np.min(dists))


# ==============================================================================
# 3. CLASS QUẢN LÝ MÔ PHỎNG (DYNAMIC SIMULATION CONTROLLER)
# ==============================================================================
class SwervingSimulation:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.time = 0.0
        self.is_paused = False
        
        # Xe Máy (Bắc -> Nam, Đi thẳng trên làn x = -1.75)
        # Bắt đầu tự nhiên cách tâm ngã tư 22m, hướng xuống Nam (theta = -pi/2)
        self.x1 = -1.75
        self.y1 = 22.0
        self.th1 = -math.pi / 2.0
        self.v1 = V_CRUISE
        self.a1 = 0.0
        self.steer1 = 0.0
        
        # Ô Tô (Nam -> Tây, Chuẩn bị rẽ trái)
        # Ô tô tiếp cận gần ngã tư (s2 = 22.5m, y2 = -9.5m) với tốc độ chuyển làn cua
        self.s2 = 22.5
        self.v2 = 4.2
        self.a2 = 0.0
        self.x2, self.y2, self.th2 = get_car2_pose_at(self.s2)
        
        # Trạng thái nhận diện và tín hiệu
        self.is_encroaching = False
        self.conflict_active = False
        self.signal_active = False
        self.ttc = 99.0
        self.min_clearance = float('inf')
        self.current_clearance = float('inf')
        self.phase_text = "TIẾP CẬN GIAO LỘ (KHÔNG ĐÈN TÍN HIỆU)"
        self.completed_loop = False
        self.loop_delay_timer = 0.0

    def step(self, dt):
        if self.is_paused:
            return
            
        if self.completed_loop:
            self.loop_delay_timer += dt
            if self.loop_delay_timer >= 1.5:
                self.reset()
            return

        # 1. TÍNH TOÁN VỊ TRÍ VÀ ĐẦU MŨI Ô TÔ (CAR NOSE & CORNERS)
        self.x2, self.y2, self.th2 = get_car2_pose_at(self.s2)
        cos2, sin2 = math.cos(self.th2), math.sin(self.th2)
        
        # Tọa độ mũi xe ô tô và các góc trước
        fl_x = self.x2 + (CAR_L/2)*cos2 - (CAR_W/2)*sin2
        fl_y = self.y2 + (CAR_L/2)*sin2 + (CAR_W/2)*cos2
        fr_x = self.x2 + (CAR_L/2)*cos2 + (CAR_W/2)*sin2
        fr_y = self.y2 + (CAR_L/2)*sin2 - (CAR_W/2)*cos2
        nose_x = self.x2 + (CAR_L/2)*cos2
        nose_y = self.y2 + (CAR_L/2)*sin2
        
        car_front_min_x = min(fl_x, fr_x, nose_x)

        # 2. NHẬN DIỆN LẤN LÀN THỰC TẾ (ENCROACHMENT DETECTION)
        # Chỉ khi đầu xe ô tô thực sự vượt qua vạch tim đường x=0 lấn vào làn thẳng (x < 0)
        self.is_encroaching = (car_front_min_x < 0.0) and (self.y2 > -7.0) and (self.x2 > -7.0)

        # Khoảng cách dọc giữa xe máy và đầu ô tô
        dy = self.y1 - nose_y
        v_rel = self.v1 + max(0.0, -self.v2 * sin2)
        self.ttc = dy / v_rel if (v_rel > 0 and dy > 0) else 99.0

        # Kích hoạt hành vi tương tác khi ô tô lấn làn và xe máy đang tiếp cận
        self.conflict_active = self.is_encroaching and (-1.8 < dy < 16.0)

        # 3. RA QUYẾT ĐỊNH ĐIỀU KHIỂN ĐỘNG HỌC (DYNAMIC DECISION & CONTROL)
        if self.conflict_active:
            # Hai xe nhận thấy nguy cơ TTC: Giảm tốc bò chậm (KHÔNG DỪNG HẲN)
            target_v1 = V_CREEP_1  # 3.3 m/s (~12 km/h)
            target_v2 = 1.3        # 1.3 m/s (~4.7 km/h - bò nhường đường)
            
            # Xe máy lách sang phía Tây (bên phải theo hướng đi) để tránh đầu ô tô
            # Mục tiêu lệch làn được tính ĐỘNG theo độ vươn của mũi ô tô
            target_x1 = min(-1.75, car_front_min_x - 1.90)
            target_x1 = max(target_x1, -5.0)  # Trong phạm vi an toàn của mặt đường
            
            self.signal_active = True
            self.phase_text = f"[TTC: {self.ttc:.1f}s] Ô TÔ LẤN LÀN -- 2 XE ĐI CHẬM, XE MÁY LÁCH CONG QUA ĐẦU XE"
        elif self.y1 < nose_y - 1.8:
            # Xe máy đã lách qua đầu xe ô tô an toàn
            target_v1 = V_CRUISE
            target_v2 = 7.0
            target_x1 = -1.75  # Trả lái mượt mà về tim làn thẳng
            self.signal_active = False
            self.phase_text = "[AN TOÀN] XE MÁY ĐÃ QUA ĐẦU Ô TÔ -- TRẢ LÁI VỀ LÀN VÀ TĂNG TỐC THOÁT GIAO LỘ"
        else:
            # Chưa lấn làn: chạy bình thường tiếp cận
            target_v1 = V_CRUISE
            target_v2 = 3.8 if self.s2 > 23.0 else 4.5
            target_x1 = -1.75
            self.signal_active = False
            self.phase_text = "TIẾP CẬN GIAO LỘ (KHÔNG ĐÈN TÍN HIỆU)"

        # 4. ĐỘNG HỌC VẬN TỐC DỌC (LONGITUDINAL DYNAMICS)
        self.a1 = np.clip((target_v1 - self.v1) * 2.5, A_DECEL_MAX, A_ACCEL_MAX)
        self.a2 = np.clip((target_v2 - self.v2) * 2.5, A_DECEL_MAX, A_ACCEL_MAX)
        
        self.v1 = max(0.5, self.v1 + self.a1 * dt)
        self.v2 = max(0.5, self.v2 + self.a2 * dt)

        # 5. MÔ HÌNH LÁI ĐỘNG HỌC XE MÁY (KINEMATIC BICYCLE MODEL)
        # e: sai số lệch ngang (cross-track error)
        # psi: sai số góc hướng so với hướng Nam (-pi/2)
        e = self.x1 - target_x1
        psi = self.th1 - (-math.pi / 2.0)
        
        # Khi e > 0 (xe đang ở phía Đông so với mục tiêu), đánh lái sang phía Tây (steer < 0)
        # Góc đánh lái được giới hạn êm ái +/- 28 độ
        self.steer1 = np.clip(-0.7 * e - 1.5 * psi, -math.radians(28), math.radians(28))
        
        # Cập nhật góc hướng và tọa độ thực tế của xe máy
        d_theta = (self.v1 / WHEELBASE_MOTO) * math.tan(self.steer1) * dt
        self.th1 += d_theta
        self.x1 += self.v1 * math.cos(self.th1) * dt
        self.y1 += self.v1 * math.sin(self.th1) * dt
        
        # Cập nhật vị trí ô tô
        self.s2 += self.v2 * dt

        # 6. TÍNH KHOẢNG CÁCH THÔNG THỦY HÌNH HỌC THỰC TẾ
        c1 = get_car_corners(self.x1, self.y1, self.th1, L=MOTO_L, W=MOTO_W)
        c2 = get_car_corners(self.x2, self.y2, self.th2, L=CAR_L, W=CAR_W)
        self.current_clearance = compute_min_clearance(c1, c2)
        if self.current_clearance < self.min_clearance:
            self.min_clearance = self.current_clearance

        # 7. KIỂM TRA HOÀN THÀNH VÒNG CHẠY
        if self.y1 < -VIEW_LIMIT and self.x2 < -VIEW_LIMIT:
            self.completed_loop = True
            self.phase_text = "[HOÀN THÀNH] ĐÃ THOÁT GIAO LỘ -- ĐANG CHUẨN BỊ LẶP LẠI..."

        self.time += dt


# ==============================================================================
# 4. THIẾT KẾ ĐỒ HỌA MÔ PHỎNG CHI TIẾT (RENDERER)
# ==============================================================================
def create_simulation_gui():
    sim = SwervingSimulation()
    
    fig = plt.figure(figsize=(10, 10), facecolor='#1E1E24')
    fig.canvas.manager.set_window_title("Mô phỏng hành vi lách mượt mà qua đầu xe")
    
    # ── Sa bàn giao lộ (Main Intersection View) ──────────────────────────────
    ax_map = fig.add_axes([0.05, 0.12, 0.90, 0.85])
    ax_map.set_aspect('equal')
    ax_map.set_facecolor('#2B2D42')  # Asphalt xám đậm
    ax_map.set_xlim(-VIEW_LIMIT, VIEW_LIMIT)
    ax_map.set_ylim(-VIEW_LIMIT, VIEW_LIMIT)
    ax_map.tick_params(colors='#8D99AE', labelsize=9)
    for spine in ax_map.spines.values():
        spine.set_color('#4A4E69')
    
    # ── Nút điều khiển tương tác (Buttons) ───────────────────────────────────
    ax_btn_pause = fig.add_axes([0.20, 0.03, 0.14, 0.05])
    ax_btn_play  = fig.add_axes([0.43, 0.03, 0.14, 0.05])
    ax_btn_reset = fig.add_axes([0.66, 0.03, 0.14, 0.05])
    
    btn_pause = Button(ax_btn_pause, '||  Tạm dừng', color='#4A4E69', hovercolor='#6C757D')
    btn_play  = Button(ax_btn_play,  '>>  Tiếp tục', color='#2A9D8F', hovercolor='#38B000')
    btn_reset = Button(ax_btn_reset, '<>  Quay lại (Reset)', color='#E76F51', hovercolor='#F77F00')
    
    for btn in [btn_pause, btn_play, btn_reset]:
        btn.label.set_color('#FFFFFF')
        btn.label.set_fontweight('bold')
        btn.label.set_fontsize(10)

    # ── HÌNH HỌC NGÃ TƯ & LÀN ĐƯỜNG CHUẨN TỈ LỆ ───────────────────────────
    L_view = VIEW_LIMIT
    W_half = HALF_ROAD
    
    # Vỉa hè 4 góc
    sidewalk_color = '#4A4E69'
    ax_map.fill([-L_view, -W_half, -W_half, -L_view], [W_half, W_half, L_view, L_view], color=sidewalk_color, alpha=0.7)
    ax_map.fill([W_half, L_view, L_view, W_half], [W_half, W_half, L_view, L_view], color=sidewalk_color, alpha=0.7)
    ax_map.fill([-L_view, -W_half, -W_half, -L_view], [-L_view, -L_view, -W_half, -W_half], color=sidewalk_color, alpha=0.7)
    ax_map.fill([W_half, L_view, L_view, W_half], [-L_view, -L_view, -W_half, -W_half], color=sidewalk_color, alpha=0.7)

    # Mép đường
    boundary_style = {'color': '#EDF2F4', 'linewidth': 2.5}
    ax_map.plot([-L_view, -W_half], [W_half, W_half], **boundary_style)
    ax_map.plot([-L_view, -W_half], [-W_half, -W_half], **boundary_style)
    ax_map.plot([W_half, L_view], [W_half, W_half], **boundary_style)
    ax_map.plot([W_half, L_view], [-W_half, -W_half], **boundary_style)
    ax_map.plot([-W_half, -W_half], [-L_view, -W_half], **boundary_style)
    ax_map.plot([W_half, W_half], [-L_view, -W_half], **boundary_style)
    ax_map.plot([-W_half, -W_half], [W_half, L_view], **boundary_style)
    ax_map.plot([W_half, W_half], [W_half, L_view], **boundary_style)

    # Vạch tim đường đôi màu vàng (Center lines)
    center_style = {'color': '#FFD166', 'linewidth': 2.0}
    ax_map.plot([-L_view, -W_half], [0, 0], **center_style)
    ax_map.plot([W_half, L_view], [0, 0], **center_style)
    ax_map.plot([0, 0], [-L_view, -W_half], **center_style)
    ax_map.plot([0, 0], [W_half, L_view], **center_style)

    # Vạch phân chia các làn (Lane divider lines)
    lane_style = {'color': '#8D99AE', 'linestyle': '--', 'linewidth': 1.2, 'alpha': 0.8}
    for offset in [-3.5, 3.5]:
        ax_map.plot([-L_view, -W_half], [offset, offset], **lane_style)
        ax_map.plot([W_half, L_view], [offset, offset], **lane_style)
        ax_map.plot([offset, offset], [-L_view, -W_half], **lane_style)
        ax_map.plot([offset, offset], [W_half, L_view], **lane_style)

    # Vùng giao cắt ngã tư
    cz_patch = patches.Rectangle((-W_half, -W_half), 2 * W_half, 2 * W_half,
                                 linewidth=1.5, edgecolor='#F72585', facecolor='#F72585',
                                 alpha=0.06, linestyle=':')
    ax_map.add_patch(cz_patch)

    # LƯU Ý: KHÔNG vẽ trước bất kỳ đường quỹ đạo nào theo yêu cầu người dùng!

    # ── ĐỒ HỌA XE VÀ CÁC THÀNH PHẦN CHI TIẾT ──────────────────────────────
    # Chi tiết Xe Máy (Màu xanh dương, có đèn pha và ghi đông để thấy rõ góc hướng)
    car1_patch = patches.Rectangle((-MOTO_L/2, -MOTO_W/2), MOTO_L, MOTO_W,
                                   facecolor='#0077B6', edgecolor='#90E0EF', linewidth=1.5, zorder=10)
    car1_roof = patches.Circle((0, 0), 0.28,
                               facecolor='#03045E', edgecolor='#00B4D8', linewidth=1.2, zorder=11)
    car1_windshield = patches.Rectangle((0.35, -0.22), 0.15, 0.44,
                                        facecolor='#CAF0F8', alpha=0.85, zorder=12)
    car1_handlebar = patches.Rectangle((0.45, -0.38), 0.08, 0.76,
                                       facecolor='#ADB5BD', zorder=12)
    car1_headlight = patches.Circle((0.85, 0.0), 0.14,
                                    facecolor='#FFE66D', edgecolor='#FFFFFF', linewidth=0.8, zorder=13)
    car1_beacon = patches.Circle((0, 0), 2.5, facecolor='#FFD166', alpha=0.0, zorder=9)
    
    # Chi tiết Ô Tô (Màu đỏ cam)
    car2_patch = patches.Rectangle((-CAR_L/2, -CAR_W/2), CAR_L, CAR_W,
                                   facecolor='#D90429', edgecolor='#FF758F', linewidth=2.0, zorder=10)
    car2_roof = patches.Rectangle((-1.1, -0.65), 2.2, 1.3,
                                  facecolor='#590D22', edgecolor='#FF4D6D', linewidth=1.2, zorder=11)
    car2_windshield = patches.Polygon([[0.8, -0.65], [1.1, -0.55], [1.1, 0.55], [0.8, 0.65]],
                                      facecolor='#CAF0F8', alpha=0.85, zorder=12)
    car2_headlight1 = patches.Circle((2.15, -0.65), 0.15, facecolor='#FFE66D', zorder=13)
    car2_headlight2 = patches.Circle((2.15,  0.65), 0.15, facecolor='#FFE66D', zorder=13)

    for p in [car1_patch, car1_roof, car1_windshield, car1_handlebar, car1_headlight, car1_beacon,
              car2_patch, car2_roof, car2_windshield, car2_headlight1, car2_headlight2]:
        ax_map.add_patch(p)

    # Nhãn hiển thị vận tốc trên xe
    car1_label = ax_map.text(0, 0, "", color='#00B4D8', fontsize=8.5, fontweight='bold',
                             ha='right', va='center', zorder=15,
                             bbox=dict(boxstyle='round,pad=0.2', facecolor='#1E1E24', edgecolor='#00B4D8', alpha=0.9))
    car2_label = ax_map.text(0, 0, "", color='#FF758F', fontsize=8.5, fontweight='bold',
                             ha='left', va='center', zorder=15,
                             bbox=dict(boxstyle='round,pad=0.2', facecolor='#1E1E24', edgecolor='#FF758F', alpha=0.9))

    # Đoạn thẳng đo khoảng cách thông thủy
    dist_line, = ax_map.plot([], [], color='#FFD166', linestyle='-', linewidth=2.0, zorder=14)
    dist_text = ax_map.text(0, 0, "", color='#FFD166', fontsize=9, fontweight='bold',
                            bbox=dict(boxstyle='round,pad=0.2', facecolor='#2B2D42', edgecolor='#FFD166', alpha=0.9),
                            ha='center', va='center', zorder=16)

    # Banner trạng thái và thông báo tín hiệu
    signal_box = ax_map.text(0.0, 24.5, "", color='#1E1E24', fontsize=10, fontweight='bold',
                             ha='center', va='center', zorder=20,
                             bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFD166', edgecolor='#FFFFFF', lw=2.0))

    # ── CÁC HÀM XỬ LÝ SỰ KIỆN NÚT BẤM ─────────────────────────────────────
    def on_pause_clicked(event):
        sim.is_paused = True
    def on_play_clicked(event):
        sim.is_paused = False
    def on_reset_clicked(event):
        sim.reset()
        
    btn_pause.on_clicked(on_pause_clicked)
    btn_play.on_clicked(on_play_clicked)
    btn_reset.on_clicked(on_reset_clicked)

    def on_key(event):
        if event.key == ' ':
            sim.is_paused = not sim.is_paused
        elif event.key in ['r', 'R']:
            sim.reset()
    fig.canvas.mpl_connect('key_press_event', on_key)

    # ── VÒNG LẶP CẬP NHẬT ANIMATION ──────────────────────────
    def update_frame(frame):
        sim.step(DT)
        
        # 1. Cập nhật tư thế Xe Máy (Vị trí & Góc hướng)
        t1 = transforms.Affine2D().rotate(sim.th1).translate(sim.x1, sim.y1) + ax_map.transData
        for p in [car1_patch, car1_roof, car1_windshield, car1_handlebar, car1_headlight]:
            p.set_transform(t1)
        
        car1_label.set_position((sim.x1 - 1.2, sim.y1))
        car1_label.set_text(f"Xe máy: {sim.v1*3.6:.1f} km/h")
        
        # 2. Cập nhật tư thế Ô Tô
        t2 = transforms.Affine2D().rotate(sim.th2).translate(sim.x2, sim.y2) + ax_map.transData
        for p in [car2_patch, car2_roof, car2_windshield, car2_headlight1, car2_headlight2]:
            p.set_transform(t2)
        
        car2_label.set_position((sim.x2 + 2.0, sim.y2 + 1.2))
        car2_label.set_text(f"Ô tô: {sim.v2*3.6:.1f} km/h")

        # 3. Cập nhật Tín hiệu Beacon trên Xe Máy và Banner
        if sim.signal_active:
            alpha_beacon = 0.25 + 0.15 * math.sin(sim.time * 12.0)
            car1_beacon.set_center((sim.x1, sim.y1))
            car1_beacon.set_alpha(alpha_beacon)
            signal_box.set_visible(True)
            signal_box.set_text(f">>> [TTC: {sim.ttc:.1f}s] Ô TÔ LẤN LÀN -- XE MÁY LÁCH MƯỢT QUA ĐẦU Ô TÔ <<<")
            signal_box.get_bbox_patch().set_facecolor('#FFD166')
            signal_box.set_color('#1E1E24')
        else:
            car1_beacon.set_alpha(0.0)
            signal_box.set_visible(True)
            if "HOÀN THÀNH" in sim.phase_text or "AN TOÀN" in sim.phase_text:
                signal_box.set_text(sim.phase_text)
                signal_box.get_bbox_patch().set_facecolor('#2A9D8F')
                signal_box.set_color('#FFFFFF')
            else:
                signal_box.set_text("GIAO LỘ TỰ QUẢN (KHÔNG ĐÈN) -- ĐANG TIẾP CẬN")
                signal_box.get_bbox_patch().set_facecolor('#4A4E69')
                signal_box.set_color('#FFFFFF')

        # 4. Cập nhật vector khoảng cách thông thủy tới mũi ô tô
        nose2_x = sim.x2 + (CAR_L / 2.0) * math.cos(sim.th2)
        nose2_y = sim.y2 + (CAR_L / 2.0) * math.sin(sim.th2)
        
        if sim.current_clearance < 14.0:
            dist_line.set_data([sim.x1, nose2_x], [sim.y1, nose2_y])
            dist_line.set_visible(True)
            mid_x = (sim.x1 + nose2_x) / 2.0
            mid_y = (sim.y1 + nose2_y) / 2.0
            dist_text.set_position((mid_x, mid_y))
            dist_text.set_text(f"Khe hở: {sim.current_clearance:.2f} m")
            dist_text.set_visible(True)
            if sim.current_clearance < 1.5:
                dist_line.set_color('#FFD166')
                dist_text.get_bbox_patch().set_edgecolor('#FFD166')
            else:
                dist_line.set_color('#00F5D4')
                dist_text.get_bbox_patch().set_edgecolor('#00F5D4')
        else:
            dist_line.set_visible(False)
            dist_text.set_visible(False)

        return [car1_patch, car1_roof, car1_windshield, car1_handlebar, car1_headlight, car1_beacon, car1_label,
                car2_patch, car2_roof, car2_windshield, car2_headlight1, car2_headlight2, car2_label,
                dist_line, dist_text, signal_box]

    ani = FuncAnimation(fig, update_frame, interval=40, blit=False, cache_frame_data=False)
    plt.show()


if __name__ == "__main__":
    print("Khởi động mô phỏng lách mượt mà qua đầu xe...")
    print("- Xe 1 (Xe máy): Đi thẳng từ Bắc xuống Nam")
    print("- Xe 2 (Ô tô): Rẽ trái từ Nam sang Tây")
    print("- Chỉ kích hoạt lách khi ô tô lấn làn qua vạch tim đường (x < 0)")
    create_simulation_gui()
