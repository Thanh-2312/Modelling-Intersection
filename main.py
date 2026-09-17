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

    W = 7.0
    half_W = W / 2
    L = SPAWN_DIST + 10.0  # Vẽ đường dài hơn điểm sinh xe 1 chút

    ax.set_xlim(-ZOOM_RANGE, ZOOM_RANGE)
    ax.set_ylim(-ZOOM_RANGE, ZOOM_RANGE)
    ax.set_title("2D Continuous Intersection Simulation (IDM & Swerving)")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")

    # 1. Vẽ ranh giới đường
    road_kwargs = {'color': 'black', 'linewidth': 2}
    ax.plot([-L, -half_W], [half_W, half_W], **road_kwargs)
    ax.plot([-L, -half_W], [-half_W, -half_W], **road_kwargs)
    ax.plot([half_W, L], [half_W, half_W], **road_kwargs)
    ax.plot([half_W, L], [-half_W, -half_W], **road_kwargs)

    ax.plot([-half_W, -half_W], [-L, -half_W], **road_kwargs)
    ax.plot([half_W, half_W], [-L, -half_W], **road_kwargs)
    ax.plot([-half_W, -half_W], [half_W, L], **road_kwargs)
    ax.plot([half_W, half_W], [half_W, L], **road_kwargs)

    # Vạch đứt phân làn giữa tim đường
    ax.plot([-L, -half_W], [0, 0], color='gray', linestyle='--', linewidth=1)
    ax.plot([half_W, L], [0, 0], color='gray', linestyle='--', linewidth=1)
    ax.plot([0, 0], [-L, -half_W], color='gray', linestyle='--', linewidth=1)
    ax.plot([0, 0], [half_W, L], color='gray', linestyle='--', linewidth=1)

    # 2. Vùng xung đột
    cz_size = W
    cz_half = cz_size / 2
    cz = patches.Rectangle((-cz_half, -cz_half), cz_size, cz_size,
                           linewidth=2, edgecolor='red', facecolor='red', alpha=0.15)
    ax.add_patch(cz)

    # 3. Vạch dừng
    stop_dist = 10.0
    stop_kwargs = {'color': 'blue', 'linewidth': 3}
    ax.plot([-stop_dist, -stop_dist], [-half_W, 0], **stop_kwargs)
    ax.plot([stop_dist, stop_dist], [0, half_W], **stop_kwargs)
    ax.plot([0, half_W], [-stop_dist, -stop_dist], **stop_kwargs)
    ax.plot([-half_W, 0], [stop_dist, stop_dist], **stop_kwargs)

    # Đèn tín hiệu (Vẽ tại 4 góc)
    light_radius = 1.0
    lights = {
        'North': patches.Circle((-half_W - 2, stop_dist), light_radius, color='red'),
        'South': patches.Circle((half_W + 2, -stop_dist), light_radius, color='red'),
        'East': patches.Circle((stop_dist, half_W + 2), light_radius, color='red'),
        'West': patches.Circle((-stop_dist, -half_W - 2), light_radius, color='red')
    }
    for l in lights.values():
        ax.add_patch(l)

    return fig, ax, lights


fig, ax, signal_lights = setup_plot()

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
            # Tìm xe cuối cùng (ở gần điểm spawn nhất) trên nhánh này
            min_s = float('inf')
            last_veh = None
            for v in vehicles:
                v_nav_state = getattr(v, 'nav_state', 'approaching')
                if getattr(v, 'origin', '') == origin and v_nav_state == 'approaching':
                    s_v, _ = controller.get_frenet_coords(v)
                    if s_v < min_s:
                        min_s = s_v
                        last_veh = v

            can_spawn = False
            spawn_v = 10.0

            if last_veh is None:
                can_spawn = True
                spawn_v = 10.0
            else:
                # Khoảng cách trống từ đầu xe mới đến đuôi xe phía trước (giả định xe mới là ô tô L=4.5m)
                bumper_gap = (min_s - last_veh.L / 2) - (-SPAWN_DIST + 4.5 / 2)
                if last_veh.v > 4.0:
                    # Xe trước đang chạy bình thường: Cần khoảng cách động an toàn (>= 15m)
                    if bumper_gap > 15.0:
                        can_spawn = True
                        spawn_v = min(10.0, max(last_veh.v, 5.0))
                else:
                    # Xe trước đang dừng/bò chậm (hàng đợi ùn ứ):
                    # Chỉ sinh thêm xe nếu khoảng trống đủ đỗ (>= 4.0m) và đặt vận tốc ban đầu = 0
                    if bumper_gap > 4.0:
                        can_spawn = True
                        spawn_v = 0.0

            if can_spawn:
                pending_queue[origin] -= 1
                new_veh = generator.spawn_vehicle(
                    origin, initial_v=spawn_v, spawn_dist=SPAWN_DIST)
                vehicles.append(new_veh)

                # Tạo hình chữ nhật đồ họa đại diện cho xe
                color = 'royalblue' if new_veh.v_type == 'Car' else 'limegreen'
                rect = patches.Rectangle((-new_veh.L/2, -new_veh.W/2), new_veh.L, new_veh.W,
                                         color=color, alpha=0.9, zorder=3)
                ax.add_patch(rect)
                vehicle_patches[new_veh] = rect

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
    for veh in vehicles:
        rect = vehicle_patches[veh]

        # Di chuyển hình chữ nhật đến tọa độ x, y và xoay góc theta
        t = transforms.Affine2D().rotate(veh.theta).translate(veh.x, veh.y)
        rect.set_transform(t + ax.transData)

        # Kiểm tra nếu xe đi vượt khỏi khung nhìn + 10m thì xóa khỏi danh sách để nhẹ bộ nhớ
        if abs(veh.x) > ZOOM_RANGE + 10 or abs(veh.y) > ZOOM_RANGE + 10:
            to_remove.append(veh)

    # Hủy xe
    for veh in to_remove:
        rect = vehicle_patches.pop(veh)
        rect.remove()
        vehicles.remove(veh)

    time_elapsed += DT
    return list(vehicle_patches.values()) + list(signal_lights.values())


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
