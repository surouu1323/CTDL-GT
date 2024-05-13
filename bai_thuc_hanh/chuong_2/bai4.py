class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr
    def NhomHang(self):
        # Kiểm tra số hàng và số cột của ma trận
        rows = len(self.arr)
        cols = len(self.arr[0])
        if rows != cols: #  kiểm tra xem số hàng và số cột của ma trận có bằng nhau hay không
            return False
        
        # Kiểm tra mỗi phần tử chứa một số nguyên của ma trận
        for i in self.arr:
            if i < [0]: # kiểm tra xem các phần tử của ma trận có phải là số nguyên không âm không
                return False

        n = len(self.arr)
        # Tạo một từ điển để lưu trữ các nhóm chỉ mục hàng
        nhom_hang = {}

        # Duyệt qua từng hàng trong ma trận
        for i in range(n):
            # Chuyển đổi hàng thành chuỗi để sử dụng làm khóa trong từ điển
            hang = str(self.arr[i])

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
mang = PhuongThuc( [[1, 2, 3],
                    [4, 5, 6],
                    [1, 2, 3],])

mang.NhomHang()

mang = PhuongThuc( [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
mang.NhomHang() 
