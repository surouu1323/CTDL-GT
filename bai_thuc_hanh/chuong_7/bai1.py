class DoThi:
    def __init__(self):
        self.ds_ke = {}  # Danh sách kề (adjacency list)

    def them_dinh(self, u):
        if u not in self.ds_ke:
            self.ds_ke[u] = []

    def them_canh(self, u, v):
        self.them_dinh(u)
        self.them_dinh(v)
        self.ds_ke[u].append(v)
        self.ds_ke[v].append(u)  # Nếu là đồ thị vô hướng

    def DFS(self, v, visited):
        visited[v] = True
        for neighbour in self.ds_ke[v]:
            if not visited[neighbour]:
                self.DFS(neighbour, visited)

    def lien_thong(self):
        visited = {v: False for v in self.ds_ke}  # Khởi tạo tất cả các đỉnh đều chưa được thăm
        start_vertex = next(iter(self.ds_ke), None)  # Chọn một đỉnh bất kỳ làm đỉnh bắt đầu
        if start_vertex is not None:
            self.DFS(start_vertex, visited)
            # Kiểm tra tất cả các đỉnh đã được thăm hay chưa
            return all(visited.values())
        return False

# Ví dụ sử dụng
dt = DoThi()
dt.them_canh(0, 1)
dt.them_canh(1, 2)
dt.them_canh(3, 4)

print(dt.lien_thong())  # Kết quả sẽ là False nếu không thêm cạnh (2, 3)

dt.them_canh(2, 3)  # Nếu thêm cạnh này thì đồ thị sẽ liên thông
print(dt.lien_thong())
