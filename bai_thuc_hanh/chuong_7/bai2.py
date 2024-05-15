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

    def SoThanhPhan(self):
        visited = {v: False for v in self.ds_ke}  # Khởi tạo tất cả các đỉnh đều chưa được thăm
        count = 0
        for vertex in self.ds_ke:
            if not visited[vertex]:
                self.DFS(vertex, visited)
                count += 1
        return count

# Ví dụ sử dụng
dt = DoThi()
dt.them_canh(0, 1)
dt.them_canh(0, 2)
dt.them_canh(1, 2)
dt.them_canh(3, 4)

print(dt.SoThanhPhan())  # Kết quả sẽ là 2 vì có 2 thành phần liên thông: {0, 1, 2} và {3, 4}
