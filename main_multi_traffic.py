import math
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
from matplotlib.animation import FuncAnimation

from vehicle import Vehicle
from generator import TrafficGenerator
from control import VehicleController
from geometry import draw_intersection
from signal_controller import SignalController

# =======================================================
# CẤU HÌNH MÔ PHỎNG (SIMULATION CONFIGURATION)
# =======================================================
SPAWN_DIST = 60.0    # Khoảng cách sinh xe ban đầu (m)
ZOOM_RANGE = 65.0    # Phạm vi khung hình (m)
DT = 0.1             # Bước thời gian (s)
LAMBDA_RATE = 0.4    # Tỷ lệ xe đến (xe/giây) cho mỗi nhánh

# Khởi tạo các module
generator = TrafficGenerator(lambda_rate=LAMBDA_RATE)
controller = VehicleController()
signal_controller = SignalController()
vehicles = []

# Quản lý thời gian sinh xe cho 4 nhánh
next_spawns = {
    'North': 0.0,
    'South': 0.0,
    'East': 0.0,
    'West': 0.0
}
pending_queue = {
    'North': 0,
    'South': 0,
    'East': 0,
    'West': 0
}
time_elapsed = 0.0

# =======================================================
# HÀM THIẾT LẬP KHUNG ĐỒ HỌA
# =======================================================


def setup_plot():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')

    # Thông số hình học ngã tư (AI.md mục 1.1)
    W = 21.0        # Chiều rộng mỗi nhánh (21m: 3 làn vào + 3 làn ra)
    half_W = W / 2  # 10.5m
    L = SPAWN_DIST + 10.0

    ax.set_xlim(-ZOOM_RANGE, ZOOM_RANGE)
    ax.set_ylim(-ZOOM_RANGE, ZOOM_RANGE)
    ax.set_title("2D Continuous Intersection Simulation (IDM + Swerving) - 6 Làn")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")

    # 1. Ranh giới đường
    road_kwargs = {'color': 'black', 'linewidth': 2}
    ax.plot([-L, -half_W], [half_W, half_W], **road_kwargs)
    ax.plot([-L, -half_W], [-half_W, -half_W], **road_kwargs)
    ax.plot([half_W, L], [half_W, half_W], **road_kwargs)
    ax.plot([half_W, L], [-half_W, -half_W], **road_kwargs)

    ax.plot([-half_W, -half_W], [-L, -half_W], **road_kwargs)
    ax.plot([half_W, half_W], [-L, -half_W], **road_kwargs)
    ax.plot([-half_W, -half_W], [half_W, L], **road_kwargs)
    ax.plot([half_W, half_W], [half_W, L], **road_kwargs)

    # Vạch tim đường (nét liền vàng)
    center_kwargs = {'color': 'goldenrod', 'linewidth': 2, 'linestyle': '-'}
    ax.plot([-L, -half_W], [0, 0], **center_kwargs)
    ax.plot([half_W, L], [0, 0], **center_kwargs)
    ax.plot([0, 0], [-L, -half_W], **center_kwargs)
    ax.plot([0, 0], [half_W, L], **center_kwargs)

    # Vạch phân làn (nét đứt xám tại 3.5m và 7.0m từ tim đường)
    lane_div_kwargs = {'color': 'gray', 'linestyle': '--', 'linewidth': 1, 'alpha': 0.7}
    for offset in [3.5, 7.0]:
        ax.plot([-L, -half_W], [-offset, -offset], **lane_div_kwargs)
        ax.plot([-L, -half_W], [offset, offset], **lane_div_kwargs)
        ax.plot([half_W, L], [-offset, -offset], **lane_div_kwargs)
        ax.plot([half_W, L], [offset, offset], **lane_div_kwargs)
        ax.plot([-offset, -offset], [-L, -half_W], **lane_div_kwargs)
        ax.plot([offset, offset], [-L, -half_W], **lane_div_kwargs)
        ax.plot([-offset, -offset], [half_W, L], **lane_div_kwargs)
        ax.plot([offset, offset], [half_W, L], **lane_div_kwargs)

    # 2. Vùng xung đột 21x21m (AI.md mục 1.1)
    cz = patches.Rectangle((-half_W, -half_W), W, W,
                           linewidth=2, edgecolor='red', facecolor='red', alpha=0.15)
    ax.add_patch(cz)

    # 3. Vạch dừng tại s = -10.5m (AI.md mục 1.1)
    stop_dist = 10.5
    stop_kwargs = {'color': 'blue', 'linewidth': 3}
    ax.plot([-stop_dist, -stop_dist], [-half_W, 0], **stop_kwargs)   # Tây vào
    ax.plot([stop_dist, stop_dist], [0, half_W], **stop_kwargs)       # Đông vào
    ax.plot([0, half_W], [-stop_dist, -stop_dist], **stop_kwargs)     # Nam vào
    ax.plot([-half_W, 0], [stop_dist, stop_dist], **stop_kwargs)      # Bắc vào

    # Đèn tín hiệu (vẽ tại góc tiếp cận)
    light_radius = 1.0
    lights = {
        'North': patches.Circle((-half_W - 2, stop_dist), light_radius, color='red'),
        'South': patches.Circle((half_W + 2, -stop_dist), light_radius, color='red'),
        'East': patches.Circle((stop_dist, half_W + 2), light_radius, color='red'),
        'West': patches.Circle((-stop_dist, -half_W - 2), light_radius, color='red')
    }
    for l in lights.values():
        ax.add_patch(l)

    status_banner = ax.text(0.0, 58.0, "DÒNG XE HỖN HỢP: ĐÈN TÍN HIỆU 2 PHA + TTC 2D LÁCH ĐỘNG HỌC",
                            color='#1E1E24', fontsize=9.5, fontweight='bold', ha='center', va='center',
                            bbox=dict(boxstyle='round,pad=0.4', facecolor='#E0E1DD', edgecolor='#FFFFFF', lw=1.5),
                            zorder=20)

    return fig, ax, lights, status_banner


fig, ax, signal_lights, status_banner = setup_plot()

# Dictionary lưu trữ đối tượng đồ họa (Patch) của từng xe
vehicle_patches = {}

# =======================================================
# VÒNG LẶP ANIMATION (Cập nhật mỗi frame)
# =======================================================


def update(frame):
    global time_elapsed

    # 1. Sinh xe mới tại 4 nhánh nếu đến lượt
    for origin in next_spawns.keys():
        if time_elapsed >= next_spawns[origin]:
            pending_queue[origin] += 1
            next_spawns[origin] += generator.generate_headway()

        # Nếu có xe đang chờ xếp hàng để vào nhánh
        if pending_queue[origin] > 0:
            candidate_veh = generator.spawn_vehicle(
                origin, initial_v=10.0, spawn_dist=SPAWN_DIST)
            cand_s, cand_d = controller.get_frenet_coords(candidate_veh)

            # Tìm xe gần điểm spawn nhất trong cùng làn (AI.md mục 2.3)
            min_s = float('inf')
            last_veh_in_lane = None
            for v in vehicles:
                v_nav_state = getattr(v, 'nav_state', 'approaching')
                if getattr(v, 'origin', '') == origin and v_nav_state == 'approaching':
                    s_v, d_v = controller.get_frenet_coords(v)
                    # Chỉ so sánh xe trong cùng làn (độ lệch ngang < 2m)
                    if abs(d_v - cand_d) < 2.0:
                        if s_v < min_s:
                            min_s = s_v
                            last_veh_in_lane = v

            can_spawn = False
            spawn_v = 10.0

            if last_veh_in_lane is None:
                # Không có xe phía trước → sinh tự do
                can_spawn = True
                spawn_v = 10.0
            else:
                # Kiểm tra khoảng cách an toàn (AI.md mục 2.3)
                bumper_gap = (min_s - last_veh_in_lane.L / 2) - \
                    (-SPAWN_DIST + candidate_veh.L / 2)
                if last_veh_in_lane.v > 4.0:
                    # Xe trước đang chạy bình thường: cần d_gap > 15m
                    if bumper_gap > 15.0:
                        can_spawn = True
                        spawn_v = min(10.0, max(last_veh_in_lane.v, 5.0))
                else:
                    # Xe trước đang dừng/bò chậm: cần d_gap > 4m, spawn v = 0
                    if bumper_gap > 4.0:
                        can_spawn = True
                        spawn_v = 0.0

            if can_spawn:
                pending_queue[origin] -= 1
                candidate_veh.v = spawn_v
                vehicles.append(candidate_veh)

                color = 'royalblue' if candidate_veh.v_type == 'Car' else 'limegreen'
                rect = patches.Rectangle((-candidate_veh.L/2, -candidate_veh.W/2),
                                         candidate_veh.L, candidate_veh.W,
                                         color=color, alpha=0.9, zorder=3)
                ax.add_patch(rect)
                vehicle_patches[candidate_veh] = rect

    # 2. Điều khiển hành vi (IDM, Swerving, Tín hiệu đèn) và Cập nhật trạng thái
    signal_controller.step(DT)
    controller.step(vehicles, DT, signal_controller)

    # Cập nhật màu đèn trên đồ họa
    color_map = {'G': 'green', 'Y': 'yellow', 'R': 'red'}
    for origin in signal_lights:
        state = signal_controller.get_state(origin)
        signal_lights[origin].set_color(color_map[state])

    # 3. Cập nhật đồ họa và Xóa xe đã ra khỏi màn hình
    to_remove = []
    active_swerving_veh = None

    for veh in vehicles:
        rect = vehicle_patches[veh]

        # Di chuyển hình chữ nhật đến tọa độ x, y và xoay góc theta
        t = transforms.Affine2D().rotate(veh.theta).translate(veh.x, veh.y)
        rect.set_transform(t + ax.transData)

        # Cập nhật màu sắc nếu đang lách qua đầu xe đối diện
        if getattr(veh, 'is_swerving', False):
            rect.set_facecolor('#FFE66D')  # Vàng phát sáng khi đang lách TTC 2D
            rect.set_edgecolor('#FF5722')
            rect.set_linewidth(2.0)
            active_swerving_veh = veh
        else:
            default_color = 'royalblue' if veh.v_type == 'Car' else 'limegreen'
            rect.set_facecolor(default_color)
            rect.set_edgecolor('none')
            rect.set_linewidth(1.0)

        # Xóa xe khi ra ngoài khu vực theo dõi (AI.md mục 2.3: |x| > 75m hoặc |y| > 75m)
        if abs(veh.x) > 75.0 or abs(veh.y) > 75.0:
            to_remove.append(veh)

    # Cập nhật banner trạng thái TTC 2D
    if active_swerving_veh is not None:
        ttc_val = getattr(active_swerving_veh, 'active_ttc', 0.0)
        status_banner.set_text(f">>> [TTC 2D: {ttc_val:.1f}s] XE MÁY ĐANG LÁCH QUA ĐẦU Ô TÔ RẼ TRÁI (LÀN BÊN CẠNH AN TOÀN) <<<")
        status_banner.get_bbox_patch().set_facecolor('#FFD166')
    else:
        status_banner.set_text("DÒNG XE HỖN HỢP: ĐÈN TÍN HIỆU 2 PHA + TTC 2D LÁCH ĐỘNG HỌC")
        status_banner.get_bbox_patch().set_facecolor('#E0E1DD')

    # Hủy xe
    for veh in to_remove:
        rect = vehicle_patches.pop(veh)
        rect.remove()
        vehicles.remove(veh)

    time_elapsed += DT
    return list(vehicle_patches.values()) + list(signal_lights.values()) + [status_banner]


# =======================================================
# CHẠY MÔ PHỎNG
# =======================================================
if __name__ == "__main__":
    print("Starting Intersection Simulation GUI...")
    print("- Car: Blue Rectangle")
    print("- Motorcycle: Green Rectangle")

    # interval=50 tức là 50ms mỗi frame (tốc độ realtime 1x với DT=0.1s thì sẽ hơi nhanh,
    # dùng interval=100 thì bằng realtime. Ta dùng 50 để chạy nhanh gấp đôi cho dễ nhìn).
    ani = FuncAnimation(fig, update, frames=2000, interval=50, blit=False)

    plt.show()
