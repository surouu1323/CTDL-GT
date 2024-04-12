def TamGiacTren(mang):
    # Kiểm tra kích thước ma trận
    n = len(mang)
    if n == 0:
        return False

    # Kiểm tra từng phần tử của ma trận
    for i in range(n):
        for j in range(i + 1, n):
            if mang[j][i] != 0:
                return False

    # Ma trận tam giác trên
    return True
mang1 = [[1, 2, 3],
         [0, 4, 5],
         [0, 0, 6]]
print(TamGiacTren(mang1))  # Kết quả: True

# Ma trận không phải tam giác trên
mang2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(TamGiacTren(mang2))  # Kết quả: False