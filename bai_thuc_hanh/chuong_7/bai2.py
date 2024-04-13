from collections import deque

def SoThanhPhan(dt):
    # Kiểm tra đồ thị rỗng
    if len(dt) == 0:
        return 0
    
    # Khởi tạo hàng đợi và tập hợp chứa các đỉnh đã duyệt
    queue = deque()
    visited = set()
    count = 0
    
    for vertex in dt:
        if vertex not in visited:
            count += 1
            queue.append(vertex)
            visited.add(vertex)
            
            while queue:
                current_vertex = queue.popleft()
                
                # Duyệt qua các đỉnh kề chưa được duyệt
                for neighbor in dt[current_vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
    
    return count

dt = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': ['E'],
    'E': ['D']
}

component_count = SoThanhPhan(dt)
print(component_count)  # Kết quả: 2