def DoiXung(mang):
    # Kiểm tra kích thước ma trận
    n = len(mang)
    if n == 0:
        return False
    # Kiểm tra từng phần tử của ma trận
    for i in range(n-1):
        for j in range(n-1):
            if mang[i][j+1] != mang[j+1][i]:
                return False
    # Ma trận đối xứng
    return True

mang1 = [[1, 2, 3],
         [2, 4, 5],
         [3, 5, 6]]
print(DoiXung(mang1))  # Kết quả: True

# Ma trận vuông không đối xứng
mang2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(DoiXung(mang2))  # Kết quả: False