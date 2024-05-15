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

    def DFS_vo_huong(self, v, visited, parent):
        visited[v] = True
        for neighbour in self.ds_ke[v]:
            if not visited[neighbour]:
                if self.DFS_vo_huong(neighbour, visited, v):
                    return True
            elif neighbour != parent:
                return True
        return False

    def DFS_huu_huong(self, v, visited, rec_stack):
        visited[v] = True
        rec_stack[v] = True
        for neighbour in self.ds_ke[v]:
            if not visited[neighbour]:
                if self.DFS_huu_huong(neighbour, visited, rec_stack):
                    return True
            elif rec_stack[neighbour]:
                return True
        rec_stack[v] = False
        return False

    def ChuTrinh(self):
        visited = {v: False for v in self.ds_ke}
        if self.huong:
            rec_stack = {v: False for v in self.ds_ke}
            for vertex in self.ds_ke:
                if not visited[vertex]:
                    if self.DFS_huu_huong(vertex, visited, rec_stack):
                        return True
        else:
            for vertex in self.ds_ke:
                if not visited[vertex]:
                    if self.DFS_vo_huong(vertex, visited, -1):
                        return True
        return False

# Ví dụ sử dụng cho đồ thị vô hướng
dt_vo_huong = DoThi(huong=False)
dt_vo_huong.them_canh(0, 1)
dt_vo_huong.them_canh(1, 2)
dt_vo_huong.them_canh(2, 0)

print(dt_vo_huong.ChuTrinh())  # Kết quả sẽ là True vì có chu trình

# Ví dụ sử dụng cho đồ thị hữu hướng
dt_huu_huong = DoThi(huong=True)
dt_huu_huong.them_canh(0, 1)
dt_huu_huong.them_canh(1, 2)
dt_huu_huong.them_canh(2, 0)

print(dt_huu_huong.ChuTrinh())  # Kết quả sẽ là True vì có chu trình
