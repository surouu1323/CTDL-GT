class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr # Khởi tạo một đối tượng PhuongThuc với một thuộc tính là một mảng arr.
        
    def Cong(self,b):
        # Chuyển đổi mảng thành số nguyên
        a = self.arr
        num_a = int(''.join(map(str, a)))
        num_b = int(''.join(map(str, b)))

        # Tính tổng
        result = num_a + num_b

        # Kiểm tra tràn số
        if result > 2 ** 31 - 1: 
            # Nếu kết quả vượt qua giới hạn của số nguyên 32-bit (2^31 - 1), trả về [-1] để chỉ ra rằng đã xảy ra tràn số.
            return [-1]

        # Phương thức trả về một số nguyên là kết quả của a + b nếu kết quả không bị tràn
        return result
    
    
a = PhuongThuc([1, 2, 3])

b = [4, 5, 6]
print(a.Cong(b))

b = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
print(a.Cong(b))