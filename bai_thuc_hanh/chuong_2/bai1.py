class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr
        
    def DoiXung(self):
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
        
        # Kiểm tra từng phần tử của ma trận
        for i in range(n):
            for j in range(i + 1, n):
                # kiểm tra xem ma trận có đối xứng qua đường chéo chính hay không 
                if self.arr[i][j] != self.arr[j][i]:
                    return False
        return True

# Ma trận vuông đối xứng
mang = PhuongThuc([ [1, 2, 3],
                    [2, 4, 5],
                    [3, 5, 6]])

print(mang.DoiXung())  # Kết quả: True

# Ma trận vuông không đối xứng
mang = PhuongThuc(  [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(mang.DoiXung())  # Kết quả: False
