import random
import math
from vehicle import Vehicle


class TrafficGenerator:
    def __init__(self, lambda_rate=0.5):
        """
        Khởi tạo Module Sinh lượng giao thông ngẫu nhiên.
        :param lambda_rate: Tỷ lệ xe đến trung bình (xe/giây) cho phần phân phối mũ.
                            VD: 0.2 nghĩa là trung bình 5 giây có 1 xe xuất hiện (không tính phần min headway).
        """
        self.lambda_rate = lambda_rate
        self.min_headway = 0.5  # Giới hạn tối thiểu thời gian giữa 2 xe (s)
        self.origins = ['North', 'South', 'East', 'West']

    def generate_headway(self):
        """
        Phát sinh khoảng thời gian giữa 2 xe liên tiếp (headway) theo phân phối Mũ bị chặn dưới (h > 1.5s).
        Quy luật: h = min_headway + Exponential(lambda_rate)
        """
        return self.min_headway + random.expovariate(self.lambda_rate)

    def generate_vehicle_type(self):
        """
        Tỷ lệ phương tiện: 50% Motorcycle, 50% Car.
        """
        v_type = random.choices(['Motorcycle', 'Car'],
                                weights=[50, 50], k=1)[0]
        return v_type

    def generate_route(self, origin):
        """
        Gán tuyến đường mục tiêu (O-D) với tỷ lệ phân luồng rẽ.
        50% Đi thẳng, 20% Rẽ phải, 30% Rẽ trái.
        :return: (hướng rẽ, đích đến)
        """
        directions = ['Straight', 'Right', 'Left']
        weights = [50, 20, 30]
        turn = random.choices(directions, weights=weights, k=1)[0]

        # Xác định đích đến (Destination) dựa vào Điểm xuất phát (Origin) và Hướng rẽ (Turn)
        destinations = {
            'North': {'Straight': 'South', 'Right': 'West', 'Left': 'East'},
            'South': {'Straight': 'North', 'Right': 'East', 'Left': 'West'},
            'East':  {'Straight': 'West', 'Right': 'North', 'Left': 'South'},
            'West':  {'Straight': 'East', 'Right': 'South', 'Left': 'North'},
        }
        destination = destinations[origin][turn]

        return turn, destination

    def spawn_vehicle(self, origin, initial_v=10.0, spawn_dist=200.0):
        """
        Tạo đối tượng xe tại điểm đầu của một nhánh đường (3 làn vào, mỗi làn rộng 3.5m).

        Quy tắc chọn làn (tính từ tim đường ra lề phải theo chiều tiến):
          Làn 1 – |d| = 1.75m (sát tim đường): CHỈ rẽ trái
          Làn 2 – |d| = 5.25m (giữa)         : rẽ trái / rẽ phải / đi thẳng
          Làn 3 – |d| = 8.75m (sát lề)        : đi thẳng / rẽ phải
        """
        v_type = self.generate_vehicle_type()
        turn, destination = self.generate_route(origin)

        # ── Chọn làn theo hướng rẽ ─────────────────────────────────────────
        if turn == 'Left':
            # Rẽ trái: ưu tiên làn 1 (sát tim đường), đôi khi dùng làn 2
            lane_center = random.choices([1.75, 5.25], weights=[70, 30])[0]
        elif turn == 'Right':
            # Rẽ phải: ưu tiên làn 3 (sát lề), đôi khi dùng làn 2
            lane_center = random.choices([8.75, 5.25], weights=[70, 30])[0]
        else:  # Straight
            # Đi thẳng: làn 2 hoặc làn 3, KHÔNG dùng làn 1 (dành cho rẽ trái)
            lane_center = random.choices([5.25, 8.75], weights=[60, 40])[0]

        target_d = -lane_center

        # Xe máy có thể lệch nhẹ trong làn (mô phỏng dòng hỗn hợp)
        if v_type == 'Motorcycle':
            # Làn rộng 3.5m, xe máy rộng 0.8m → lệch an toàn tối đa ≈ ±1.3m
            target_d += random.uniform(-1.3, 1.3)

        L = spawn_dist

        # Tọa độ khởi tạo và Góc hướng (Theta)
        # Việt Nam: đi bên PHẢI tim đường theo chiều tiến
        # → target_d âm (d < 0) tương ứng với phía bên phải
        if origin == 'West':      # Từ Tây sang Đông (theta = 0)
            x = -L
            y = target_d          # y âm = phía Nam (bên phải khi đi Đông)
            theta = 0.0
        elif origin == 'East':    # Từ Đông sang Tây (theta = π)
            x = L
            y = -target_d         # y dương = phía Bắc (bên phải khi đi Tây)
            theta = math.pi
        elif origin == 'South':   # Từ Nam lên Bắc (theta = π/2)
            x = -target_d         # x dương = phía Đông (bên phải khi đi Bắc)
            y = -L
            theta = math.pi / 2
        elif origin == 'North':   # Từ Bắc xuống Nam (theta = −π/2)
            x = target_d          # x âm = phía Tây (bên phải khi đi Nam)
            y = L
            theta = -math.pi / 2
        else:
            raise ValueError("Origin must be North, South, East, or West")

        # Khởi tạo phương tiện
        veh = Vehicle(v_type, x=x, y=y, v=initial_v, a=0.0, theta=theta)

        # Gán thông tin định tuyến và làn chuẩn
        veh.origin = origin
        veh.destination = destination
        veh.turn_direction = turn
        veh.target_d = target_d

        return veh


# ==========================================
# Khối mã kiểm thử (Test) nhanh
# ==========================================
if __name__ == "__main__":
    generator = TrafficGenerator(lambda_rate=0.2)

    print("--- Test Traffic Generator ---")

    # 1. Test Headway
    print("\n[1] Generate 5 Headways:")
    for i in range(5):
        hw = generator.generate_headway()
        print(f"  Headway {i+1}: {hw:.2f} s")

    # 2. Test Spawning Vehicles
    print("\n[2] Spawn 5 random vehicles at 'West' origin:")
    for i in range(5):
        veh = generator.spawn_vehicle('West', initial_v=12.0)
        print(f"  Veh {i+1}: {veh.v_type:<10} | Route: {veh.origin}->{veh.destination} ({veh.turn_direction:<8}) | Lane d={veh.target_d:.2f}m | Pos: ({veh.x:.1f}, {veh.y:.1f})")
