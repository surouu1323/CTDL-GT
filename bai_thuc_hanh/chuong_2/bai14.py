class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr   # Khởi tạo một đối tượng PhuongThuc với một thuộc tính là một mảng arr.
        
    def DayConDauTien(self, b):
        c = []  # Mảng chứa dãy con đầu tiên
        a = self.arr
        i = 0
        while i < len(a):
            # nếu a[i] cũng có trong mảng b, chúng ta bắt đầu kiểm tra dãy con từ vị trí hiện tại trong arr.
            if a[i] in b:
                c.append(a[i])

                # Kiểm tra dãy con từ vị trí hiện tại trong a
                j = b.index(a[i]) + 1 # trả về vị trí của giá trị a[i] trong mảng b
                k = i + 1
                
                # Nếu tìm thấy một dãy con giống với b, trả về dãy con đó
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