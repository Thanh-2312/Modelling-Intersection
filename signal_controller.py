class SignalController:
    def __init__(self):
        """
        Khởi tạo bộ điều khiển tín hiệu đèn 2 pha.
        Chu kỳ C = 80s:
        - Pha 1 (Bắc - Nam): 37s Xanh, 3s Vàng, 40s Đỏ.
        - Pha 2 (Đông - Tây): 37s Xanh, 3s Vàng, 40s Đỏ.
        """
        self.cycle_time = 80.0
        self.phase1_green = 37.0
        self.phase1_yellow = 3.0
        self.phase2_green = 37.0
        self.phase2_yellow = 3.0
        
        self.current_time = 0.0

    def step(self, dt):
        """Cập nhật thời gian trong chu kỳ đèn."""
        self.current_time = (self.current_time + dt) % self.cycle_time

    def get_state(self, origin):
        """
        Trả về trạng thái đèn ('G', 'Y', 'R') cho một hướng tới (origin) cụ thể.
        """
        t = self.current_time
        
        if origin in ['North', 'South']:
            # Pha 1: 0 -> 37 (Xanh), 37 -> 40 (Vàng), 40 -> 80 (Đỏ)
            if 0 <= t < self.phase1_green:
                return 'G'
            elif self.phase1_green <= t < (self.phase1_green + self.phase1_yellow):
                return 'Y'
            else:
                return 'R'
        elif origin in ['East', 'West']:
            # Pha 2: 0 -> 40 (Đỏ), 40 -> 77 (Xanh), 77 -> 80 (Vàng)
            phase1_duration = self.phase1_green + self.phase1_yellow
            if 0 <= t < phase1_duration:
                return 'R'
            elif phase1_duration <= t < (phase1_duration + self.phase2_green):
                return 'G'
            else:
                return 'Y'
        
        return 'R'
