import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_intersection():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')

    W = 7.0        # Chiều rộng mỗi nhánh (7m: 1 làn vào + 1 làn ra)
    L = 200.0      # Độ dài tiếp cận (200m)
    half_W = W / 2  # 3.5m

    # Giới hạn trục tọa độ (Zoom vào khu vực trung tâm để nhìn rõ vạch dừng và vùng xung đột)
    zoom_range = 200.0
    ax.set_xlim(-zoom_range, zoom_range)
    ax.set_ylim(-zoom_range, zoom_range)

    ax.set_title(
        "2D Continuous Intersection Geometry (2 Lanes Total: 1 In, 1 Out)")
    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")

    # 1. Vẽ ranh giới đường (Road Boundaries)
    road_kwargs = {'color': 'black', 'linewidth': 2}

    # Nhánh Ngang (West & East)
    ax.plot([-L, -half_W], [half_W, half_W], **road_kwargs)   # Tây - trên
    ax.plot([-L, -half_W], [-half_W, -half_W], **road_kwargs)  # Tây - dưới
    ax.plot([half_W, L], [half_W, half_W], **road_kwargs)     # Đông - trên
    ax.plot([half_W, L], [-half_W, -half_W], **road_kwargs)   # Đông - dưới

    # Nhánh Dọc (South & North)
    ax.plot([-half_W, -half_W], [-L, -half_W], **road_kwargs)  # Nam - trái
    ax.plot([half_W, half_W], [-L, -half_W], **road_kwargs)   # Nam - phải
    ax.plot([-half_W, -half_W], [half_W, L], **road_kwargs)   # Bắc - trái
    ax.plot([half_W, half_W], [half_W, L], **road_kwargs)     # Bắc - phải

    # Vẽ vạch phân cách giữa tim đường
    ax.plot([-L, -half_W], [0, 0], color='gray', linestyle='--', linewidth=1)
    ax.plot([half_W, L], [0, 0], color='gray', linestyle='--', linewidth=1)
    ax.plot([0, 0], [-L, -half_W], color='gray', linestyle='--', linewidth=1)
    ax.plot([0, 0], [half_W, L], color='gray', linestyle='--', linewidth=1)

    # 2. Vẽ Vùng Xung Đột (Conflict Zone là phần giao của 4 ngả đường: 7x7m)
    cz_size = W
    cz_half = cz_size / 2
    conflict_zone = patches.Rectangle((-cz_half, -cz_half), cz_size, cz_size,
                                      linewidth=2, edgecolor='red', facecolor='red', alpha=0.15,
                                      label=f'Conflict Zone ({W}x{W}m)')
    ax.add_patch(conflict_zone)

    # 3. Vẽ Vạch Dừng (Stop Lines) cách tâm 10m
    stop_dist = 10.0
    stop_kwargs = {'color': 'blue', 'linewidth': 3}

    # Giả định xe đi bên phải, vạch dừng phủ trọn làn vào (rộng 3.5m)
    # Nhánh Tây (Đi từ Trái sang Phải)
    ax.plot([-stop_dist, -stop_dist], [-half_W, 0],
            label='Stop Line', **stop_kwargs)
    # Nhánh Đông (Đi từ Phải sang Trái)
    ax.plot([stop_dist, stop_dist], [0, half_W], **stop_kwargs)
    # Nhánh Nam (Đi từ Dưới lên Trên)
    ax.plot([0, half_W], [-stop_dist, -stop_dist], **stop_kwargs)
    # Nhánh Bắc (Đi từ Trên xuống Dưới)
    ax.plot([-half_W, 0], [stop_dist, stop_dist], **stop_kwargs)

    # Đánh dấu tâm (0,0)
    ax.plot(0, 0, marker='+', color='black',
            markersize=10, label='Center (0,0)')

    ax.legend(loc='upper right')
    ax.grid(True, linestyle=':', alpha=0.6)

    # Lưu ra file ảnh
    output_filename = 'intersection_2d.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"Saved image to file: {output_filename}")

    # Nếu chạy script trực tiếp, có thể hiển thị
    # plt.show()


if __name__ == "__main__":
    draw_intersection()
