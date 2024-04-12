def Cong(a, b, c, d):
    # Lấy phần dấu của a và b
    sign_a = a // 10
    sign_b = b // 10

    # Lấy phần số của a và b
    num_a = a % 10
    num_b = b % 10

    # Thực hiện phép cộng
    result = (sign_a * num_a) + (sign_b * num_b)

    # Kiểm tra tràn số
    if result < -9 or result > 9:
        return [-1]

    return result
a = 0  # Số dương
b = [6, 2, 1] 
print(Cong(a, b))  # Kết quả: 1

c = 1  # Số âm
c = [5, 4, 3]
print(Cong(c, d))  # Kết quả: [-1] (vì kết quả bị tràn)