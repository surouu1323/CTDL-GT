class PhuongThuc:
    def __init__(self,BieuThuc):
        self.BieuThuc = BieuThuc
    
    def HauTo(self):
        toan_hang_stack = [] # Stack lưu trữ các toán hạng (số)
        toan_tu_stack = []  # Stack lưu trữ các toán tử (+ - * /)
        muc_do_uu_tien = {'+':1, '-':1, '*':2, '/':2 } # Độ ưu tiên của các toán tử
        
        # Tách biểu thức thành các token sử dụng split()
        tokens = self.BieuThuc.split() 
        
        for token in tokens:
            if token.isdigit(): # Nếu token là số, đưa vào stack toán hạng
                toan_hang_stack.append(token)
            else: # Nếu token là toán tử
                # Sử dụng get với từ điển muc_do_uu_tien để tránh lỗi khi gặp các ký tự không phải là toán tử.
                while (toan_tu_stack and muc_do_uu_tien.get(token,0) <= muc_do_uu_tien.get(toan_tu_stack[-1],0)):
                    toan_hang_stack.append(toan_tu_stack.pop())
                toan_tu_stack.append(token)
                
        while toan_tu_stack: # Đưa các toán tử còn lại vào stack toán hạng
            toan_hang_stack.append(toan_tu_stack.pop())
        return ' '.join(toan_hang_stack) # Trả về chuỗi biểu thức hậu tố


# Tạo một biểu thức số học
bt = PhuongThuc('2 * 3 + 5 / 5')

# Chuyển đổi sang dạng hậu tố
bt_hau_to = bt.HauTo() # 2 3 * 5 5 / +

print(bt_hau_to)