class PhuongThuc:
    def __init__(self, arr, sign):
        self.arr = arr  
        self.sign = sign
        
    def getSign(self):
        return 1 if self.sign == 0 else -1
        
    def Nhan(self, b):
        num_a = int(''.join(map(str, self.arr)))
        num_b = int(''.join(map(str, b.arr)))
        
        # Tính tổng
        result = self.getSign()*num_a * num_b*b.getSign()

        # Kiểm tra tràn số
        if result > 2 ** 31 - 1 or result < -2 ** 31 - 1:
            return [-1]

        # Phương thức trả về một số nguyên là kết quả của a + b nếu kết quả không bị tràn
        return result
    
a = PhuongThuc([1, 2, 3],0)  
b = PhuongThuc([6, 2, 1],1) 
print(a.Nhan(b))  

b = PhuongThuc([3, 1, 4, 7, 4, 8, 3, 6, 4, 8],0)
print(a.Nhan(b))  