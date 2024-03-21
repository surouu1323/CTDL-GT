def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)


a = int(input("Nhập  a: "))
b = int(input("Nhập  b: "))

result_recursive =GCD(a, b)

print("GCD cua", a, "va", b, ":", result_recursive)

