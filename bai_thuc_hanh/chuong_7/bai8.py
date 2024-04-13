def DuongDi(dt, v1, v2):
    visited = set()  # Tập hợp các đỉnh đã được duyệt
    return DFS(dt, v1, v2, visited)

def DFS(dt, current_vertex, target_vertex, visited):
    visited.add(current_vertex)

    if current_vertex == target_vertex:
        return True

    for neighbor in dt[current_vertex]:
        if neighbor not in visited:
            if DFS(dt, neighbor, target_vertex, visited):
                return True
    
    return False

dt = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A', 'B']
}

has_path = DuongDi(dt, 'A', 'D')
print(has_path)  # Kết quả: True

has_path = DuongDi(dt, 'C', 'A')
print(has_path)  # Kết quả: False