class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr
    def TrungHang(self):
        # Kiểm tra số hàng và số cột của ma trận
        rows = len(self.arr)
        cols = len(self.arr[0])
        if rows != cols: #  kiểm tra xem số hàng và số cột của ma trận có bằng nhau hay không
            return False
        
        n = len(self.arr)
        
        # Kiểm tra mỗi phần tử chứa một số nguyên của ma trận
        for i in self.arr:
            if i < [0]: # kiểm tra xem các phần tử của ma trận có phải là số nguyên không âm không
                return False

        # Kiểm tra từng cặp hàng trong ma trận
        for i in range(n):
            for j in range(i + 1, n):
                if self.arr[i] == self.arr[j]: # kiểm tra xem có hai hàng nào trong ma trận có giá trị bằng nhau không
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