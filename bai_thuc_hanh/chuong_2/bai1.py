class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr
    def DoiXung(self):
        # Kiểm tra số hàng và số cột của ma trận
        rows = len(self.arr)
        cols = len(self.arr[0])
        if rows != cols:
            return False
        
        n = len(self.arr)
        
        # Kiểm tra mỗi phần tử chứa một số nguyên của ma trận
        for i in self.arr:
            if i < [0]:
                return False
        
        # Kiểm tra từng phần tử của ma trận
        for i in range(n):
            for j in range(i + 1, n):
                if self.arr[i][j] != self.arr[j][i]:
                    return False
        return True

# Ma trận vuông đối xứng
mang = PhuongThuc([[1, 2, 3],
                    [2, 4, 5],
                    [3, 5, 6]])

print(mang.DoiXung())  # Kết quả: True

# Ma trận vuông không đối xứng
mang = PhuongThuc(  [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(mang.DoiXung())  # Kết quả: True
