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
    
    def GiaTri(self):
        bieu_thuc_hau_to = self.HauTo().split()
        tinh_stack= []
        for toan_tu in bieu_thuc_hau_to:
            if toan_tu.isdigit(): # Nếu token là số, đưa vào stack tính toán
                tinh_stack.append(float(toan_tu))
            else:
                b = tinh_stack.pop() # Lấy 2 số từ stack
                a = tinh_stack.pop()
                tinh_stack.append(self.apply_operation(toan_tu,a,b)) # Thực hiện phép toán và đưa kết quả lại vào stack
                
        print(tinh_stack.pop()) # In kết quả cuối cùng
                
    def apply_operation(self, operator, a, b):
        # Thực hiện phép toán
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            # Sử dụng phép chia thực (float division) để tránh lỗi chia cho 0
            return a / b
        


# Tạo một biểu thức số học
bt = PhuongThuc('2 * 3 / 4 + 8 - 2 + 1 ')

bt.GiaTri()# Tính giá trị của biểu thức và in kết quả = 8.5


bt = PhuongThuc('2 + 3 * 4')
bt.GiaTri()# Tính giá trị của biểu thức và in kết quả = 14