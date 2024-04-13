class BieuThuc:
    def __init__(self, bt):
        self.bt = bt

    def GiaTri(self):
        toan_hang_stack = []
        toan_tu_stack = []
        i = 0
        while i < len(self.bt):
            if self.bt[i].isdigit():
                toan_hang = ""
                while i < len(self.bt) and self.bt[i].isdigit():
                    toan_hang += self.bt[i]
                    i += 1
                toan_hang_stack.append(int(toan_hang))
            elif self.bt[i] in ['+', '-', '*', '/']:
                while (
                    toan_tu_stack and
                    self.DieuKienUuTien(self.bt[i], toan_tu_stack[-1])
                ):
                    self.TinhToan(toan_hang_stack, toan_tu_stack)
                toan_tu_stack.append(self.bt[i])
                i += 1

        while toan_tu_stack:
            self.TinhToan(toan_hang_stack, toan_tu_stack)

        return toan_hang_stack[-1]

    def DieuKienUuTien(self, op1, op2):
        if op2 == '(' or op2 == ')':
            return False
        if (op1 == '*' or op1 == '/') and (op2 == '+' or op2 == '-'):
            return False
        return True

    def TinhToan(self, toan_hang_stack, toan_tu_stack):
        toan_tu = toan_tu_stack.pop()
        toan_hang2 = toan_hang_stack.pop()
        toan_hang1 = toan_hang_stack.pop()

        if toan_tu == '+':
            toan_hang_stack.append(toan_hang1 + toan_hang2)
        elif toan_tu == '-':
            toan_hang_stack.append(toan_hang1 - toan_hang2)
        elif toan_tu == '*':
            toan_hang_stack.append(toan_hang1 * toan_hang2)
        elif toan_tu == '/':
            toan_hang_stack.append(toan_hang1 / toan_hang2)


# Tạo một biểu thức
bt = "3+4*2/(1-5)"

# Tính giá trị của biểu thức
bieu_thuc = BieuThuc(bt)
gia_tri = bieu_thuc.GiaTri()
print("Giá trị của biểu thức:", gia_tri)