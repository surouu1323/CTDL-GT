def SoCungVao(dt, v):
    count = 0
    for vertex in dt:
        if v in dt[vertex]:
            count += 1
    return count

dt = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A', 'B']
}

in_degree = SoCungVao(dt, 'D')
print(in_degree)  # Kết quả: 2

in_degree = SoCungVao(dt, 'E')
print(in_degree)  # Kết quả: 0