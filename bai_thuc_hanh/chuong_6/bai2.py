def Hieu(a, b):
    set_a = set(a)  # Tạo tập hợp từ mảng a
    set_b = set(b)  # Tạo tập hợp từ mảng b
    difference = set_a - set_b  # Lấy hiệu của hai tập hợp
    sorted_difference = sorted(difference)  # Sắp xếp kết quả theo thứ tự tăng dần
    return sorted_difference

a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hieu(a, b)
print(c)