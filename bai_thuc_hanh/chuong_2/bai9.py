def TrungCot(mang):
    cols = len(mang[0])
    rows = len(mang)

    for i in range(cols):
        for j in range(i + 1, cols):
            column_i = [mang[k][i] for k in range(rows)]
            column_j = [mang[k][j] for k in range(rows)]
            if column_i == column_j:
                return True

    return False
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(TrungCot(matrix1))  # Kết quả: False (không có hai cột giống nhau)

matrix2 = [
    [1, 2, 1],
    [4, 5, 4],
    [7, 8, 7]
]
print(TrungCot(matrix2))  # Kết quả: True (có hai cột giống nhau)