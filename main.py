"""
MÔ PHỎNG VI MÔ HÀNH VI LÁCH MƯỢT MÀ QUA ĐẦU XE (SMOOTH SWERVING SIMULATION)
===========================================================================
Chương trình chính (Entrypoint):
1. Chế độ mặc định:
   Mô phỏng kịch bản 2 xe tương tác tại ngã tư không đèn:
   - Xe 1: Đi thẳng từ làn Bắc đến Nam (Xanh dương).
   - Xe 2: Rẽ trái từ làn Nam sang Tây (Đỏ cam).
   - Tính toán TTC tránh va chạm.
   - Khi vào vùng xung đột, CẢ HAI XE ĐI CHẬM LẠI, KHÔNG DỪNG HẲN.
   - Tín hiệu kích hoạt khi Xe 1 lách mượt mà qua đầu Xe 2.
   - Chuẩn tỉ lệ hình học thực tế (L_xe = 4.6m, W_xe = 1.8m, W_làn = 3.5m).
   - Nút tương tác: [ ⏸ Tạm dừng ], [ ▶ Tiếp tục ], [ 🔄 Quay lại ].

2. Chế độ sinh dòng xe hỗn hợp liên tục (Multi-Traffic):
   Chạy với cờ: python main.py --multi (hoặc chạy trực tiếp main_multi_traffic.py)
"""

import sys
from smooth_swerving_sim import create_simulation_gui


def main():
    if len(sys.argv) > 1 and sys.argv[1] in ['--multi', '-m', '--traffic']:
        print("Đang khởi động chế độ mô phỏng dòng xe hỗn hợp liên tục (main_multi_traffic.py)...")
        import subprocess
        subprocess.run([sys.executable, "main_multi_traffic.py"])
    else:
        print("=" * 70)
        print("KHỞI ĐỘNG MÔ PHỎNG HÀNH VI LÁCH MƯỢT MÀ QUA ĐẦU XE (BẮC-NAM & NAM-TÂY)")
        print("=" * 70)
        print("- Kịch bản: 1 Xe đi thẳng Bắc -> Nam và 1 Xe rẽ trái Nam -> Tây.")
        print("- Giao lộ tự quản: Không có đèn tín hiệu, tự né nhau bằng TTC.")
        print("- Hành vi: Cả 2 xe đều đi chậm lại trong vùng va chạm (KHÔNG DỪNG HẲN).")
        print("- Tín hiệu lách xe: Hiển thị nổi bật khi Xe 1 lách qua đầu Xe 2.")
        print("- Tỉ lệ thực tế: Chiều dài ô tô 4.60m, Làn đường 3.50m (Tỉ lệ 1.31x).")
        print("- Phím tắt: [Space]: Tạm dừng/Tiếp tục | [R]: Quay lại (Reset) | [Q]: Thoát.")
        print("=" * 70)
        create_simulation_gui()


if __name__ == "__main__":
    main()
