def TamGiacDuoi(mang):
    # Kiểm tra số hàng và số cột của ma trận
    rows = len(mang)
    cols = len(mang[0])
    if rows != cols:
        return False

    # Kiểm tra các phần tử nằm trên đường chéo chính và trên đường chéo phụ
    for i in range(rows):
        for j in range(i + 1, cols):
            if mang[i][j] != 0:
                return False

    return True
matrix1 = [
    [1, 0, 0],
    [2, 3, 0],
    [4, 5, 6]
]
print(TamGiacDuoi(matrix1))  # Kết quả: True (là ma trận tam giác dưới)

matrix2 = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]
print(TamGiacDuoi(matrix2))  # Kết quả: False (không là ma trận tam giác dưới)