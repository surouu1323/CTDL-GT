def Duynhat(a):
    unique_numbers = list(set(a))  # Lấy danh sách các số duy nhất từ mảng a
    unique_numbers.sort()  # Sắp xếp các số duy nhất theo thứ tự tăng dần
    return unique_numbers
a = [1, 5, 3, 7, 5, 9, 7]
b = Duynhat(a)
print(b)