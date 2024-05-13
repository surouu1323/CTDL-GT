def GCD(a, b):
    # Nếu b bằng 0, a chính là GCD của a và b, vì a chia hết cho b và do đó a là ước chung lớn nhất.
    if b == 0:
        return a
    else:
    # b không bằng 0, sử dụng thuật toán Euclid để tìm GCD. 
    # Thuật toán này làm cho b trở thành a, và a % b trở thành b, và lặp lại quá trình này cho đến khi b trở thành 0. 
    # Khi đó, a sẽ là GCD của a và b.
        return GCD(b, a%b)


a = int(input("Nhập  a: "))
b = int(input("Nhập  b: "))

result_recursive =GCD(a, b)

print("GCD cua", a, "va", b, ":", result_recursive)

