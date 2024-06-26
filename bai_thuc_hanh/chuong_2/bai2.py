class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr
        
    def TamGiacTren(self):
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
                if self.arr[j][i] != 0: # kiểm tra từng phần tử của ma trận để xem xét nếu có bất kỳ phần tử nào nằm dưới đường chéo chính khác 0.
                    return False
        return True
    
 # Ma trận tam giác trên    
mang = PhuongThuc(  [[1, 2, 3],
                    [0, 4, 5],
                    [0, 0, 6]])

print(mang.TamGiacTren())  

# Ma trận không phải tam giác trên
mang = PhuongThuc(  [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

print(mang.TamGiacTren()) 