def NhomHang(mang):
    # Kiểm tra kích thước ma trận
    n = len(mang)
    if n == 0:
        return

    # Tạo một từ điển để lưu trữ các nhóm chỉ mục hàng
    nhom_hang = {}

    # Duyệt qua từng hàng trong ma trận
    for i in range(n):
        # Chuyển đổi hàng thành chuỗi để sử dụng làm khóa trong từ điển
        hang = str(mang[i])

        # Nếu hàng đã tồn tại trong từ điển, thêm chỉ mục hàng vào nhóm tương ứng
        if hang in nhom_hang:
            nhom_hang[hang].append(i)
        else:
            # Nếu hàng chưa tồn tại, tạo một nhóm mới với chỉ mục hàng hiện tại
            nhom_hang[hang] = [i]

    # In ra các nhóm chỉ mục hàng
    for nhom in nhom_hang.values():
        print("Nhóm chỉ mục hàng:", nhom)
# Ma trận với các hàng giống nhau
mang1 = [[1, 2, 3],
         [4, 5, 6],
         [1, 2, 3],
         [7, 8, 9],
         [4, 5, 6]]
NhomHang(mang1)
# Kết quả:
# Nhóm chỉ mục hàng: [0, 2]
# Nhóm chỉ mục hàng: [1, 4]

# Ma trận không có hàng giống nhau
mang2 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
NhomHang(mang2)
# Kết quả:
# Không có nhóm chỉ mục hàng