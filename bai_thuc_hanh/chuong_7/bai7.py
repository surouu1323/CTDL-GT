class DoThi:
    def __init__(self, huong=False):
        self.ds_ke = {}  # Danh sách kề (adjacency list)
        self.huong = huong  # Biến để xác định đồ thị có hướng hay không

    def them_canh(self, u, v):
        if u not in self.ds_ke:
            self.ds_ke[u] = []
        if v not in self.ds_ke:
            self.ds_ke[v] = []
        self.ds_ke[u].append(v)
        if not self.huong:
            self.ds_ke[v].append(u)

    def ChuaDinh(self, v):
        return v in self.ds_ke

    def SoCungVao(self, v):
        if not self.huong:
            return None  # Phương thức chỉ áp dụng cho đồ thị hữu hướng
        count = 0
        for u in self.ds_ke:
            if v in self.ds_ke[u]:
                count += 1
        return count

    def SoCungRa(self, v):
        if not self.huong:
            return None  # Phương thức chỉ áp dụng cho đồ thị hữu hướng
        if v not in self.ds_ke:
            return 0  # Nếu đỉnh không tồn tại trong đồ thị
        return len(self.ds_ke[v])

# Ví dụ sử dụng
dt_huu_huong = DoThi(huong=True)
dt_huu_huong.them_canh(0, 1)
dt_huu_huong.them_canh(2, 1)
dt_huu_huong.them_canh(3, 1)
dt_huu_huong.them_canh(1, 2)

print(dt_huu_huong.SoCungRa(0))  # Kết quả sẽ là 1 vì có 1 cung đi ra từ đỉnh 0 (tới 1)
print(dt_huu_huong.SoCungRa(1))  # Kết quả sẽ là 1 vì có 1 cung đi ra từ đỉnh 1 (tới 2)
print(dt_huu_huong.SoCungRa(2))  # Kết quả sẽ là 1 vì có 1 cung đi ra từ đỉnh 2 (tới 1)
print(dt_huu_huong.SoCungRa(3))  # Kết quả sẽ là 1 vì có 1 cung đi ra từ đỉnh 3 (tới 1)
print(dt_huu_huong.SoCungRa(4))  # Kết quả sẽ là 0 vì đỉnh 4 không có trong đồ thị
