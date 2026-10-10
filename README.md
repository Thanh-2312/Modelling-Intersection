# Mô phỏng vi mô nút giao thông hỗn hợp 2D (2D Continuous Mixed-Traffic Simulation)

Dự án mô phỏng động học vi mô nút giao thông bao gồm:
1. **Mô phỏng hành vi lách mượt mà qua đầu xe tại ngã tư không đèn tín hiệu (`smooth_swerving_sim.py` / `main.py`)**: Kịch bản tương tác chính xác giữa 1 xe đi thẳng (Bắc - Nam) và 1 xe rẽ trái (Nam - Tây).
2. **Mô phỏng dòng xe hỗn hợp liên tục đa làn (`main_multi_traffic.py`)**: Dòng xe ô tô và xe máy phát sinh ngẫu nhiên có đèn tín hiệu 2 pha.

![Mô phỏng lách mượt mà qua đầu xe](swerving_snapshot.png)

---

## 📌 1. Kịch bản lách mượt mà qua đầu xe (`main.py` / `smooth_swerving_sim.py`)

Kịch bản tập trung nghiên cứu hành vi tương tác né tránh giữa 2 phương tiện tại nút giao không đèn tín hiệu:

- **Hai phương tiện tương tác:**
  - **Xe 1 (Xe máy - Xanh dương):** Kích thước chuẩn $L = 2.00\text{ m}, W = 0.80\text{ m}$, đi thẳng từ Bắc xuống Nam ($x = -1.75\text{ m}$).
  - **Xe 2 (Ô tô - Đỏ cam):** Kích thước chuẩn $L = 4.60\text{ m}, W = 1.80\text{ m}$, rẽ trái từ làn Nam sang nhánh Tây qua đường cong Bézier.
- **Tự né tránh bằng chỉ số TTC 2D (Time-To-Collision):**
  - **Chỉ kích hoạt khi lấn làn:** Chỉ khi đầu mũi hoặc góc trái ô tô vượt qua vạch tim đường $x = 0$ sang phía làn thẳng ($x < 0$), tín hiệu TTC 2D mới được kích hoạt giữa hai xe.
  - Không vẽ trước quỹ đạo hay cố định hành vi.
- **Hành vi giảm tốc bò chậm -- TUYỆT ĐỐI KHÔNG DỪNG HẲN:**
  - Cả hai phương tiện giảm tốc êm ái xuống mức bò chậm:
    - Xe máy: $v_1 \approx 12\text{ km/h}$ ($3.3\text{ m/s}$).
    - Ô tô: $v_2 \approx 4.7\text{ km/h}$ ($1.3\text{ m/s}$).
  - Cả hai xe luôn duy trì vận tốc dương ($v > 0$), không bị dừng chết tại chỗ.
- **Động học lách cong mượt mà (Kinematic Steering):**
  - Xe máy dùng mô hình động học xe đạp (Bicycle Steering) đánh lái nghiêng đầu xe về phía Tây ($\theta \approx -102^\circ \sim -105^\circ$), tạo thành quỹ đạo cong mượt mà dạt sang phải lách qua trước đầu mũi ô tô với khoảng cách an toàn thông thủy $> 1.3\text{ m}$.
  - Sau khi vượt qua mũi ô tô, xe máy tự động hoàn trả góc lái về làn thẳng và cả hai xe cùng tăng tốc thoát giao lộ.
- **Chuẩn tỉ lệ hình học thực tế:**
  - Bề rộng làn đường tiêu chuẩn: $W_{\text{làn}} = 3.50\text{ m}$.
  - Ô tô: $4.60\text{ m} \times 1.80\text{ m}$. Xe máy: $2.00\text{ m} \times 0.80\text{ m}$.
  - Nút tương tác: `|| Tạm dừng`, `>> Tiếp tục`, `<> Quay lại (Reset)`.

---

## 📌 2. Mô phỏng dòng xe hỗn hợp liên tục đa làn (`main_multi_traffic.py` / `python main.py --multi`)

- **Tích hợp cơ chế TTC 2D & Lách động học vào môi trường đa xe:**
  - Xe máy đi thẳng khi gặp ô tô rẽ trái đối diện lấn qua vạch tim đường sẽ kích hoạt tính toán TTC 2D.
  - **Kiểm tra khe hở bên sườn (Lateral Gap Acceptance):** Xe máy chỉ lách sang làn bên cạnh khi làn bên cạnh thông thoáng (không có xe chạy song song). Nếu làn bên cạnh bị chiếm chỗ, xe máy tự động giảm tốc bò nhường đường trong làn để tránh va quẹt bên sườn.
  - **Hiển thị trực quan:** Xe máy đang lách TTC 2D phát sáng viền cam nổi bật cùng banner thông báo thời gian thực.

---

## 📂 2. Cấu trúc mã nguồn

```text
Modelling_Itersection/
├── main.py                 # Khởi chạy mô phỏng lách mượt mà qua đầu xe (Mặc định)
├── smooth_swerving_sim.py  # Module mô phỏng kịch bản lách xe, tính TTC, đồ họa & nút tương tác
├── main_multi_traffic.py   # Bản lưu mô phỏng dòng xe hỗn hợp liên tục đa làn (có đèn)
├── vehicle.py              # Định nghĩa lớp Vehicle và mô hình động học
├── generator.py            # Sinh lưu lượng xe ngẫu nhiên (Poisson/Headway) & gán tuyến (O-D)
├── control.py              # Bộ điều khiển xe: IDM, Swerving, Bézier navigation, xử lý xung đột
├── signal_controller.py    # Bộ điều khiển chu kỳ đèn tín hiệu 2 pha
├── geometry.py             # Bản vẽ tĩnh cấu trúc nút giao thông 2D
├── requirements.txt        # Các thư viện phụ thuộc (matplotlib, numpy)
└── README.md               # Tài liệu hướng dẫn dự án
```

---

## 🚀 3. Hướng dẫn chạy chương trình

### Yêu cầu:
Python 3.8+ và các thư viện trong `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Chạy mô phỏng lách mượt mà qua đầu xe:
```bash
python main.py
```
*(hoặc `python smooth_swerving_sim.py`)*

### Chạy mô phỏng dòng xe hỗn hợp ngẫu nhiên nhiều làn:
```bash
python main.py --multi
```
*(hoặc `python main_multi_traffic.py`)*
