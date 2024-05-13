class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr # Khởi tạo một đối tượng PhuongThuc với một thuộc tính là một mảng arr.
        
    def TamGiacDuoi(self):
        # Kiểm tra số hàng và số cột của ma trận
        rows = len(self.arr)
        cols = len(self.arr[0])
        if rows != cols: # kiểm tra xem số hàng và số cột của ma trận có bằng nhau hay không. 
            return False
        
        # Kiểm tra mỗi phần tử chứa một số nguyên của ma trận
        for i in self.arr:
            if i < [0]: # kiểm tra xem các phần tử của ma trận có phải là số nguyên không âm không
                return False

        # Kiểm tra các phần tử nằm trên đường chéo chính và trên đường chéo phụ
        for i in range(rows):
            for j in range(i + 1, cols):
                if self.arr[i][j] != 0: # kiểm tra xem các phần tử nằm trên đường chéo chính và phía trên đường chéo chính có bằng 0 không
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