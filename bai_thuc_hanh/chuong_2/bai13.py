class PhuongThuc:
    def __init__(self, arr, sign):
        self.arr = arr   # Khởi tạo một đối tượng PhuongThuc với một thuộc tính là một mảng arr.
        self.sign = sign # Khởi tạo một đối tượng PhuongThuc với một thuộc tính là dấu.
        
    def getSign(self):
        return 1 if self.sign == 0 else -1 # Trả về 1 nếu sign là 0 (dương) và trả về -1 nếu sign là 1 (âm).
        
    def Nhan(self, b):
        # các mảng số nguyên của hai đối tượng được chuyển đổi thành số nguyên để thực hiện phép cộng.
        num_a = int(''.join(map(str, self.arr)))
        num_b = int(''.join(map(str, b.arr)))
        
        # Tính tổng
        result = self.getSign()*num_a * num_b*b.getSign()
        # tổng của hai số nguyên này được tính toán, với việc áp dụng dấu của từng số bằng cách sử dụng phương thức getSign().

        # Kiểm tra tràn số
        if result > 2 ** 31 - 1 or result < -2 ** 31 - 1:
            # Nếu kết quả vượt qua giới hạn của số nguyên 32-bit (2^31 - 1), trả về [-1] để chỉ ra rằng đã xảy ra tràn số.
            return [-1]

        # Phương thức trả về một số nguyên là kết quả của a + b nếu kết quả không bị tràn
        return result
    
a = PhuongThuc([1, 2, 3],0)  
b = PhuongThuc([6, 2, 1],1) 
print(a.Nhan(b))  

b = PhuongThuc([3, 1, 4, 7, 4, 8, 3, 6, 4, 8],0)
print(a.Nhan(b))  