def Hop(a, b):
    set_a = set(a)  # Tạo tập hợp từ mảng a
    set_b = set(b)  # Tạo tập hợp từ mảng b
    union = set_a.union(set_b)  # Lấy hợp của hai tập hợp
    sorted_union = sorted(union)  # Sắp xếp kết quả theo thứ tự tăng dần
    return sorted_union

a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hop(a, b)
print(c)