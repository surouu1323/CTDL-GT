def Tru(a, b):
    # Chuyển đổi mảng thành số nguyên
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))

    # Tính hiệu
    result = num_a - num_b
    
    # Kiểm tra tràn số
    if result < 0:
        return [-1]

    # Chuyển đổi kết quả thành mảng số nguyên
    result_arr = list(map(int, str(result)))

    return result_arr
a = [3, 2, 1]
b = [1, 0, 0]
print(Tru(a, b))  # Kết quả: [2, 2, 1]

c = [5, 4, 3]
d = [6, 0, 0]
print(Tru(c, d))  # Kết quả: [-1] (vì a < b)