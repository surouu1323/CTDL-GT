def SoCungRa(dt, v):
    count = 0
    for vertex in dt[v]:
        count += 1
    return count

dt = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['A', 'B']
}

out_degree = SoCungRa(dt, 'B')
print(out_degree)  # Kết quả: 2

out_degree = SoCungRa(dt, 'E')
print(out_degree)  # Kết quả: 0