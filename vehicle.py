import math

class Vehicle:
    def __init__(self, v_type, x=0.0, y=0.0, v=0.0, a=0.0, theta=0.0):
        """
        Khởi tạo đối tượng phương tiện giao thông.
        
        :param v_type: 'Car' hoặc 'Motorcycle'
        :param x: Tọa độ x (m)
        :param y: Tọa độ y (m)
        :param v: Vận tốc hiện tại (m/s)
        :param a: Gia tốc hiện tại (m/s^2)
        :param theta: Góc hướng di chuyển (radians, 0 là hướng trục Ox dương)
        """
        self.v_type = v_type
        
        if self.v_type == 'Car':
            self.L = 4.5             # Chiều dài xe (m)
            self.W = 1.8             # Chiều rộng xe (m)
            self.v_max = 50 / 3.6    # Tốc độ tối đa (m/s) ~ 13.89 m/s
        elif self.v_type == 'Motorcycle':
            self.L = 1.8             # Chiều dài xe máy (m)
            self.W = 0.8             # Chiều rộng xe máy (m)
            self.v_max = 40 / 3.6    # Tốc độ tối đa (m/s) ~ 11.11 m/s
        else:
            raise ValueError("Loại xe không hợp lệ. Vui lòng chọn 'Car' hoặc 'Motorcycle'.")
            
        # Trạng thái động học
        self.x = x
        self.y = y
        self.v = v
        self.a = a
        self.theta = theta
        
        # Giới hạn vật lý (áp dụng chung cho cả hai loại theo yêu cầu)
        self.a_max = 2.5       # Gia tốc tăng tốc tối đa (m/s^2)
        self.a_comf = -3.0     # Gia tốc phanh thoải mái (m/s^2)
        self.a_min = -5.0      # Gia tốc phanh khẩn cấp (m/s^2)
        
        # Biến trạng thái cho Vùng Lưỡng Lự và Gap Acceptance
        self.dilemma_decision = None # 'Stop', 'Go', or None
        
    def set_acceleration(self, new_a):
        """
        Thiết lập gia tốc mới, tự động cắt (clip) theo giới hạn vật lý.
        """
        self.a = max(self.a_min, min(new_a, self.a_max))
        
    def update_state(self, dt=0.1):
        """
        Cập nhật trạng thái vị trí và vận tốc sau mỗi bước thời gian dt.
        """
        # Cập nhật vận tốc dự kiến
        v_next = self.v + self.a * dt
        
        # Giới hạn vận tốc: không được chạy lùi (v < 0) và không vượt quá v_max
        v_next = max(0.0, min(v_next, self.v_max))
        
        # Tính quãng đường di chuyển trong dt (sử dụng vận tốc trung bình để chính xác hơn)
        if self.v == 0.0 and v_next == 0.0:
            ds = 0.0
        else:
            ds = (self.v + v_next) / 2.0 * dt
            
        # Cập nhật vị trí
        self.x += ds * math.cos(self.theta)
        self.y += ds * math.sin(self.theta)
        
        # Lưu vận tốc mới
        self.v = v_next

    def __repr__(self):
        return f"{self.v_type}(x={self.x:.2f}, y={self.y:.2f}, v={self.v:.2f}m/s, a={self.a:.2f}m/s^2)"

# ==========================================
# Khối mã kiểm thử (Test) nhanh
# ==========================================
if __name__ == "__main__":
    # Tạo 1 xe ô tô đang chạy hướng Ox
    car = Vehicle('Car', x=-10, y=-1.75, v=10.0, a=2.0, theta=0.0)
    print("Initial state:", car)
    
    # Cập nhật 1 giây (10 bước x 0.1s)
    for _ in range(10):
        car.update_state(dt=0.1)
    
    print("After 1s acceleration (a=2.0):", car)
    
    # Cho phanh thoải mái
    car.set_acceleration(-3.0)
    for _ in range(20):  # 2 giây
        car.update_state(dt=0.1)
        
    print("After 2s braking (a=-3.0):", car)
