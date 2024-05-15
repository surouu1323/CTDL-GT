class DoThi:
    def __init__(self):
        self.ds_ke = {}  # Danh sách kề (adjacency list)

    def them_canh(self, u, v):
        if u not in self.ds_ke:
            self.ds_ke[u] = []
        if v not in self.ds_ke:
            self.ds_ke[v] = []
        self.ds_ke[u].append(v)
        self.ds_ke[v].append(u)  # Nếu là đồ thị vô hướng

    def DFS(self, v, visited):
        visited[v] = True
        for neighbour in self.ds_ke[v]:
            if not visited[neighbour]:
                self.DFS(neighbour, visited)

    def LienThong(self):
        visited = {v: False for v in self.ds_ke}  # Khởi tạo tất cả các đỉnh đều chưa được thăm
        # Bắt đầu duyệt từ đỉnh đầu tiên trong danh sách
        start_vertex = next(iter(self.ds_ke))
        self.DFS(start_vertex, visited)
        # Kiểm tra tất cả các đỉnh đã được thăm hay chưa
        for vertex in visited:
            if not visited[vertex]:
                return False
        return True

# Ví dụ sử dụng
dt = DoThi()
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(1, 2)
dt.them_canh(2, 3)
# dt.them_canh(3, 4)  # Nếu bạn thêm cạnh này thì đồ thị sẽ liên thông

print(dt.LienThong())  # Kết quả sẽ là False nếu không thêm cạnh (3, 4)
