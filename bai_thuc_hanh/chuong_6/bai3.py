def Giao(a, b):
    set_a = set(a)  # Tạo tập hợp từ mảng a
    set_b = set(b)  # Tạo tập hợp từ mảng b
    intersection = set_a.intersection(set_b)  # Lấy giao của hai tập hợp
    sorted_intersection = sorted(intersection)  # Sắp xếp kết quả theo thứ tự tăng dần
    return sorted_intersection

a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Giao(a, b)
print(c)