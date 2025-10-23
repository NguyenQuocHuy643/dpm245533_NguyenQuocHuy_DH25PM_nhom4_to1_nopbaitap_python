def thuc_hien_phep_toan(a, b, phep_toan):
    """
    Thực hiện phép tính cơ bản (+, -, *, /) giữa hai số a và b.
    """
    
    # Chuyển đổi a và b thành số thực (float) để xử lý cả số nguyên và số thập phân.
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return "Lỗi: Giá trị a hoặc b nhập vào không phải là số hợp lệ."
    
    # Thực hiện phép toán dựa trên toán tử nhập vào
    if phep_toan == '+':
        ket_qua = a + b
    elif phep_toan == '-':
        ket_qua = a - b
    elif phep_toan == '*':
        ket_qua = a * b
    elif phep_toan == '/':
        # Xử lý trường hợp chia cho 0
        if b == 0:
            return "Lỗi: Không thể chia cho 0."
        ket_qua = a / b
    else:
        return f"Lỗi: Phép toán '{phep_toan}' không hợp lệ. Chỉ chấp nhận '+', '-', '*', '/'."
    
    # Trả về kết quả
    return f"Kết quả của {a} {phep_toan} {b} là: {ket_qua}"

# --- Phần nhập dữ liệu từ người dùng và hiển thị kết quả ---

print("--- CHƯƠNG TRÌNH MÁY TÍNH CƠ BẢN ---")

try:
    so_a = input("Nhập giá trị a: ")
    so_b = input("Nhập giá trị b: ")
    toan_tu = input("Nhập phép toán (+, -, *, /): ")
    
    # Gọi hàm và in kết quả
    ket_qua_cuoi = thuc_hien_phep_toan(so_a, so_b, toan_tu.strip())
    print("-" * 35)
    print(ket_qua_cuoi)
    print("-" * 35)
    
except Exception as e:
    # Xử lý các lỗi khác ngoài logic của hàm (ví dụ: lỗi hệ thống)
    print(f"Đã xảy ra lỗi không xác định: {e}")