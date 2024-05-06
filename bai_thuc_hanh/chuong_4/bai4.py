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

# Tạo một biểu thức số học
bt = PhuongThuc('2 * 3 + 5 / 5')

# Chuyển đổi sang dạng hậu tố
bt_hau_to = bt.HauTo()

print(bt_hau_to)