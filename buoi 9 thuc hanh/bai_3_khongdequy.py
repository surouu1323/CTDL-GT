def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhập m: "))
b = int(input("Nhập n: "))

result_non_recursive = GCD(a, b)
print("GCD()", a, "và", b, "là:", result_non_recursive)
