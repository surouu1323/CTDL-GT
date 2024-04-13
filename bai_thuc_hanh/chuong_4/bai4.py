class BieuThuc:
    def __init__(self, bt):
        self.bt = bt

    def HauTo(self):
        toan_hang_stack = []
        toan_tu_stack = []
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        tokens = self.bt.split()

        for token in tokens:
            if token.isdigit():
                toan_hang_stack.append(token)
            else:
                while (toan_tu_stack and precedence[token] <= precedence.get(toan_tu_stack[-1], 0)):
                    toan_hang_stack.append(toan_tu_stack.pop())
                toan_tu_stack.append(token)

        while toan_tu_stack:
            toan_hang_stack.append(toan_tu_stack.pop())

        return ' '.join(toan_hang_stack)


# Tạo một biểu thức số học
bieu_thuc = BieuThuc('2 + 8 / 5')

# Chuyển đổi sang dạng hậu tố
bieu_thuc_hau_to = bieu_thuc.HauTo()

print(bieu_thuc_hau_to)