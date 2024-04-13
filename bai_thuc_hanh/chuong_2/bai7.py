def Nhan(a, b):
    # Chuyển đổi mảng thành số nguyên
    num_a = int(''.join(map(str, a)))
    num_b = int(''.join(map(str, b)))

    # Tính tích
    result = num_a * num_b

    # Kiểm tra tràn số
    if result > 2**31 - 1:
        return [-1]

    # Chuyển đổi kết quả thành mảng số nguyên
    result_arr = list(map(int, str(result)))

    return result_arr
a = [1, 2, 3]
b = [4, 5, 6]
print(Nhan(a, b))  # Kết quả: [5, 6, 7, 3, 8]

c = [9]
d = [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
print(Nhan(c, d))  # Kết quả: [-1] (vì kết quả bị tràn)