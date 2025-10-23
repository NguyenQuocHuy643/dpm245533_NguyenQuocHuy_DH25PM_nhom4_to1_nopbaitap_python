# Nhập vào ngày, tháng, năm
try:
    ngay = int(input("Nhập ngày (D): "))
    thang = int(input("Nhập tháng (M): "))
    nam = int(input("Nhập năm (Y): "))

    # Tạo đối tượng datetime từ thông tin nhập
    ngay_hien_tai = datetime(nam, thang, ngay)
    
    # Sử dụng timedelta để cộng thêm 1 ngày
    ngay_ke_sau = ngay_hien_tai + timedelta(days=1)
    
    # In kết quả theo định dạng D/M/Y
    ket_qua = ngay_ke_sau.strftime("%d/%m/%Y")
    
    print(f"\nNgày đã nhập là: {ngay}/{thang}/{nam}")
    print(f"Ngày kế sau là: {ket_qua}")

except ValueError:
    print("Lỗi: Dữ liệu nhập vào không hợp lệ hoặc ngày không tồn tại.")
except Exception as e:
    print(f"Đã xảy ra lỗi: {e}")