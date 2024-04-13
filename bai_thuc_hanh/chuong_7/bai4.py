def ChuaDinh(dt, v):
    return v in dt

dt = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

has_vertex = ChuaDinh(dt, 'C')
print(has_vertex)  # Kết quả: True

has_vertex = ChuaDinh(dt, 'E')
print(has_vertex)  # Kết quả: False