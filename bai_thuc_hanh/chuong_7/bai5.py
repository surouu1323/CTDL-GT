def BacDinh(dt, v):
    if v in dt:
        return len(dt[v])
    else:
        return 0
    
dt = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

degree = BacDinh(dt, 'B')
print(degree)  # Kết quả: 3

degree = BacDinh(dt, 'E')
print(degree)  # Kết quả: 0