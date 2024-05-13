class PhuongThuc:
    def __init__(self, matrix):
        self.matrix = matrix
            
    def _DienTich(self,matrix, visited, row, col):
        # Kiểm tra giới hạn của ma trận và trạng thái đã thăm
        if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]) or visited[row][col] or matrix[row][col] == 0:
            return 0

        # Đánh dấu ô đã thăm
        visited[row][col] = True

        # Đệ quy kiểm tra các ô kề cạnh
        count = 1
        count += self._DienTich(matrix, visited, row + 1, col)  # Kiểm tra ô phía dưới
        count += self._DienTich(matrix, visited, row - 1, col)  # Kiểm tra ô phía trên
        count += self._DienTich(matrix, visited, row, col + 1)  # Kiểm tra ô bên phải
        count += self._DienTich(matrix, visited, row, col - 1)  # Kiểm tra ô bên trái
        return count


    def Dao(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        max_area = 0  # Diện tích lớn nhất của các đảo hình chữ nhật

        # Tạo ma trận visited để lưu trạng thái đã thăm
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                # có được đánh dấu đã thăm chưa (visited[row][col]), và có phải là đất liền không (matrix[row][col] == 0)
                if not visited[row][col] and self.matrix[row][col] == 1:
                    area = self._DienTich(self.matrix, visited, row, col)
                    max_area = max(max_area, area)

        return max_area

mang = PhuongThuc([ [1, 0, 1, 1, 0],
                    [1, 1, 0, 0, 1],
                    [0, 1, 0, 1, 1],
                    [0, 0, 0, 1, 1],
                    [1, 1, 1, 0, 1]])

print(mang.Dao())  # Kết quả: 6
