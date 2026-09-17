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
        Tỷ lệ phương tiện: 67% Motorcycle, 33% Car (để tổng = 100%).
        """
        # Sử dụng random.choices với trọng số
        v_type = random.choices(['Motorcycle', 'Car'],
                                weights=[67, 33], k=1)[0]
        return v_type

    def generate_route(self, origin):
        """
        Gán tuyến đường mục tiêu (O-D) với tỷ lệ phân luồng rẽ.
        70% Đi thẳng, 20% Rẽ phải, 10% Rẽ trái.
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
        Tạo đối tượng xe tại điểm đầu của một nhánh đường chỉ định (1 làn vào mỗi nhánh, tâm làn cách tim đường 1.75m).
        :param origin: 'North', 'South', 'East', 'West'
        :param initial_v: Vận tốc khởi tạo (m/s)
        :param spawn_dist: Khoảng cách khởi tạo tính từ tâm ngã tư (m)
        """
        v_type = self.generate_vehicle_type()
        turn, destination = self.generate_route(origin)

        # Tâm làn đi cách tim đường 1.75m (nửa đường rộng 3.5m)
        lane_center = 1.75
        target_d = -lane_center
        L = spawn_dist

        # Tọa độ khởi tạo và Góc hướng (Theta)
        # Giả định Việt Nam đi bên phải tim đường theo chiều tiến
        if origin == 'West':      # Từ Tây sang Đông
            x = -L
            y = -lane_center
            theta = 0.0
        elif origin == 'East':    # Từ Đông sang Tây
            x = L
            y = lane_center
            theta = math.pi
        elif origin == 'South':   # Từ Nam lên Bắc
            x = lane_center
            y = -L
            theta = math.pi / 2
        elif origin == 'North':   # Từ Bắc xuống Nam
            x = -lane_center
            y = L
            theta = -math.pi / 2
        else:
            raise ValueError("Origin must be North, South, East, or West")

        # Khởi tạo phương tiện từ class Vehicle
        veh = Vehicle(v_type, x=x, y=y, v=initial_v, a=0.0, theta=theta)

        # Gán thêm thông tin định tuyến (O-D) và tọa độ làn chuẩn
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
        print(f"  Veh {i+1}: {veh.v_type:<10} | Route: {veh.origin}->{veh.destination} ({veh.turn_direction:<8}) | Pos: ({veh.x}, {veh.y})")
