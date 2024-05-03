class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr    
    def TrungCot(self):
        # Kiểm tra số hàng và số cột của ma trận
        rows = len(self.arr)
        cols = len(self.arr[0])
        if rows != cols:
            return False
        
        # Kiểm tra mỗi phần tử chứa một số nguyên của ma trận
        for i in self.arr:
            if i < [0]:
                return False
        
        cols = len(self.arr[0])
        rows = len(self.arr)

        for i in range(cols):
            for j in range(i + 1, cols):
                column_i = [self.arr[k][i] for k in range(rows)]
                column_j = [self.arr[k][j] for k in range(rows)]
                if column_i == column_j:
                    return True

        return False
 
mang = PhuongThuc([ [1, 2, 1],
                    [4, 5, 4],
                    [7, 8, 7]])
print(mang.TrungCot()) 
    
mang = PhuongThuc([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(mang.TrungCot())

