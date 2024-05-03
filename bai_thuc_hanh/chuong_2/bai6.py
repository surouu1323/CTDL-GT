class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr
    def Tru(self,b):
        # Chuyển đổi mảng thành số nguyên
        a = self.arr
        num_a = int(''.join(map(str, a)))
        num_b = int(''.join(map(str, b)))

        # Tính hiệu
        result = num_a - num_b
        
        # Kiểm tra tràn số
        if result < -2 ** 31 - 1:
            return [-1]

        # Phương thức trả về một số nguyên là kết quả của a + b nếu kết quả không bị tràn
        return result
    
    
a = PhuongThuc([1, 2, 3])

b = [1, 0, 0]
print(a.Tru(b))

b = [3, 1, 4, 7, 4, 8, 3, 6, 4, 8]
print(a.Tru(b))