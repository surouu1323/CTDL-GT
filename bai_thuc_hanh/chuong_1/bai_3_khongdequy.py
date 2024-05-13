def GCD(a, b):
    # Sử dụngvòng lặp while để lặp cho đến khi b trở thành 0.
    while b != 0:
        # gán a =b , và b = a % b 
        a, b = b, a % b
    # Khi b = 0, kết thúc vòng lặp và trả về a, a chính là GCD của a và b.
    return a

a = int(input("Nhập m: "))
b = int(input("Nhập n: "))

result_non_recursive = GCD(a, b)
print("GCD()", a, "và", b, "là:", result_non_recursive)
