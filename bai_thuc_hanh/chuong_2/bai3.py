class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr
    def TrungHang(self):
        # Kiểm tra kích thước ma trận
        n = len(self.arr)
        if n == 0:
            return False
        
        n = len(self.arr)
        
        # Kiểm tra mỗi phần tử chứa một số nguyên của ma trận
        for i in self.arr:
            if i < [0]:
                return False

        # Kiểm tra từng cặp hàng trong ma trận
        for i in range(n):
            for j in range(i + 1, n):
                if self.arr[i] == self.arr[j]:
                    return True
        # Không có hai hàng giống nhau
        return False
    
# Ma trận có hai hàng giống nhau
 # Ma trận tam giác trên    
mang = PhuongThuc( [[1, 2, 3],
                    [4, 5, 6],
                    [1, 2, 3]])

print(mang.TrungHang())  

# Ma trận không có hai hàng giống nhau
mang = PhuongThuc([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(mang.TrungHang()) 