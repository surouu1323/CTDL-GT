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

# Ví dụ sử dụng
dt = DoThi(huong=False)
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(1, 2)
dt.them_canh(2, 3)

print(dt.ChuaDinh(1))  # Kết quả sẽ là True vì đỉnh 1 có trong đồ thị
print(dt.ChuaDinh(4))  # Kết quả sẽ là False vì đỉnh 4 không có trong đồ thị
