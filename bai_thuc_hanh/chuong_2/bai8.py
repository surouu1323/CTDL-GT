class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr
        
    def TamGiacDuoi(self):
        # Kiểm tra số hàng và số cột của ma trận
        rows = len(self.arr)
        cols = len(self.arr[0])
        if rows != cols:
            return False
        
        # Kiểm tra mỗi phần tử chứa một số nguyên của ma trận
        for i in self.arr:
            if i < [0]:
                return False

        # Kiểm tra các phần tử nằm trên đường chéo chính và trên đường chéo phụ
        for i in range(rows):
            for j in range(i + 1, cols):
                if self.arr[i][j] != 0:
                    return False
        return True

mang = PhuongThuc(  [[1, 0, 0],
                    [2, 3, 0],
                    [4, 5, 6]])
print(mang.TamGiacDuoi())

mang = PhuongThuc([ [1, 2, 3],
                    [0, 4, 5],
                    [0, 0, 6]])
print(mang.TamGiacDuoi())