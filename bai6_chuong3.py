def doc_so_hai_chu_so(n):
    
    if not (0 <= n <= 99):
        return "Lỗi: Số nhập vào phải nằm trong phạm vi từ 0 đến 99."
    
  
    don_vi = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
 
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", 
                 "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    if n == 0:
        return "không"
        
    if n < 10:
        return don_vi[n]
    chuc = n // 10  
    le = n % 10     
    ket_qua = hang_chuc[chuc]
   
    if le > 0:
        phan_le = ""
        
        if le == 1:
            if chuc == 1: 
                phan_le = "một"
            else:        
                phan_le = "mốt"

        elif le == 5 and chuc >= 2:
            phan_le = "lăm"
        elif le == 4 and chuc == 1: 
            phan_le = "tư"
        else:
            phan_le = don_vi[le]
        ket_qua = f"{ket_qua} {phan_le}"
    return ket_qua
cac_so_can_kiem_tra = [5, 35, 10, 14, 15, 21, 99, 30, 0, 1]
print("===================================")
print("  KIỂM TRA CHUYỂN ĐỔI SỐ SANG CHỮ")
print("===================================")
for so in cac_so_can_kiem_tra:
    doc_chu = doc_so_hai_chu_so(so)
    print(f"Số {so: <3} => {doc_chu}")
print("===================================")