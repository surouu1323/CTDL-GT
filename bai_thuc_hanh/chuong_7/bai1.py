from collections import deque

def LienThong(dt):
    # Kiểm tra đồ thị rỗng
    if len(dt) == 0:
        return False
    
    # Chọn một đỉnh bất kỳ để bắt đầu duyệt
    start_vertex = next(iter(dt))
    
    # Khởi tạo hàng đợi và tập hợp chứa các đỉnh đã duyệt
    queue = deque([start_vertex])
    visited = set([start_vertex])
    
    while queue:
        current_vertex = queue.popleft()
        
        # Duyệt qua các đỉnh kề chưa được duyệt
        for neighbor in dt[current_vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    # Kiểm tra xem tất cả các đỉnh đã được duyệt
    return len(visited) == len(dt)

dt = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B'],
    'D': ['E'],
    'E': ['D']
}

is_connected = LienThong(dt)
print(is_connected)  # Kết quả: True