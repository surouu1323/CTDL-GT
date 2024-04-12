def TrungHang(mang):
    # Kiểm tra kích thước ma trận
    n = len(mang)
    if n == 0:
        return False

    # Kiểm tra từng cặp hàng trong ma trận
    for i in range(n):
        for j in range(i + 1, n):
            if mang[i] == mang[j]:
                return True

    # Không có hai hàng giống nhau
    return False
# Ma trận có hai hàng giống nhau
mang1 = [[1, 2, 3],
         [4, 5, 6],
         [1, 2, 3]]
print(TrungHang(mang1))  # Kết quả: True

# Ma trận không có hai hàng giống nhau
mang2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
print(TrungHang(mang2))  # Kết quả: False