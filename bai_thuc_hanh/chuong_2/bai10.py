class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr    
    def NhomCot(self):
        # Kiểm tra số hàng và số cột của ma trận
        rows = len(self.arr)
        cols = len(self.arr[0])
        if rows != cols:
            return False
        
        # Kiểm tra mỗi phần tử chứa một số nguyên của ma trận
        for i in self.arr:
            if i < [0]:
                return False

        # Tạo một từ điển để lưu trữ các nhóm chỉ mục hàng
        nhom_cot = {}

        # Duyệt qua từng cột trong ma trận
        for i in range(cols):
            for j in range(rows):
                # Chuyển đổi cột thành chuỗi để sử dụng làm khóa trong từ điển
                cot = str(self.arr[j][i])
                # Nếu cột đã tồn tại trong từ điển, thêm chỉ mụcvào nhóm tương ứng
            if cot in nhom_cot:
                nhom_cot[cot].append(i)
            else:
                # Nếu chưa tồn tại, tạo một nhóm mới với chỉ mục hiện tại
                nhom_cot[cot] = [i]
        # In ra các nhóm chỉ mục hàng
        for nhom in nhom_cot.values():
            print("Nhóm chỉ mục cột:", nhom)
            
 
mang = PhuongThuc([ [1, 2, 1],
                    [4, 5, 4],
                    [7, 8, 7]])
mang.NhomCot()
    
mang = PhuongThuc([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
mang.NhomCot()

