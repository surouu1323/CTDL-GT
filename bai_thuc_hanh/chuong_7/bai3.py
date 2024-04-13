def ChuTrinh(dt):
    # Khởi tạo tập hợp chứa các đỉnh đã duyệt
    visited = set()
    
    for vertex in dt:
        if vertex not in visited:
            if has_cycle(dt, vertex, visited, parent=None):
                return True
    
    return False

def has_cycle(dt, current_vertex, visited, parent):
    visited.add(current_vertex)
    
    for neighbor in dt[current_vertex]:
        if neighbor not in visited:
            if has_cycle(dt, neighbor, visited, current_vertex):
                return True
        elif neighbor != parent:
            return True
    
    return False

dt = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['D'],
    'D': ['A'],
    'E': []
}

has_cycle = ChuTrinh(dt)
print(has_cycle)  # Kết quả: True