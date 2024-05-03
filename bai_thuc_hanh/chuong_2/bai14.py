class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr  
    def DayConDauTien(self, b):
        c = []  # Mảng chứa dãy con đầu tiên
        a = self.arr
        i = 0
        while i < len(a):
            if a[i] in b:
                c.append(a[i])

                # Kiểm tra dãy con từ vị trí hiện tại trong a
                j = b.index(a[i]) + 1
                k = i + 1

                while j < len(b) and k < len(a) and a[k] == b[j]:
                    c.append(a[k])
                    j += 1
                    k += 1

                if len(c) > 0:
                    return c

                c = []  # Reset mảng c nếu không tìm thấy dãy con

            i += 1

        return c
    
a = PhuongThuc([1, 6, 2, 4, 5, 7, 9, 4, 2])
b = [9, 6, 2, 5, 3, 7, 8]
print(a.DayConDauTien(b))