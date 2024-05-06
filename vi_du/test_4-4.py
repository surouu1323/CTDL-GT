class PhuongThuc:
    def __init__(self,BieuThuc):
        self.BieuThuc = BieuThuc
    
    def HauTo(self):
        toan_hang_stack = [] # là số
        toan_tu_stack = []  # là + - * /
        muc_do_uu_tien = {'+':1, '-':1, '*':2, '/':2 }
        
        tokens = self.BieuThuc.split()
        for token in tokens:
            if token.isdigit():
                toan_hang_stack.append(token)
            else:
                while (toan_tu_stack and muc_do_uu_tien[token] <= muc_do_uu_tien[toan_tu_stack[-1]]):
                    toan_hang_stack.append(toan_tu_stack.pop())
                toan_tu_stack.append(token)
        while toan_tu_stack:
            toan_hang_stack.append(toan_tu_stack.pop())
        return ' '.join(toan_hang_stack)
    
    def GiaTri(self):
        bieu_thuc_hau_to = self.HauTo()
        tinh_stack= []
        for toan_tu in bieu_thuc_hau_to:
            if toan_tu.isdigit():
                tinh_stack.append(toan_tu)
            elif toan_tu != ' ':
                b = float(tinh_stack.pop())
                a = float(tinh_stack.pop())
                tinh_stack.append(float(self.apply_operation(toan_tu,a,b)))
                
        print(tinh_stack.pop())
                
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

print(bt.HauTo())
bt.GiaTri()