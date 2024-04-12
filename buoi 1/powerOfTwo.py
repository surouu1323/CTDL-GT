def powerOfTwo(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2

n = int(input("nhap n: "))
ketqua = powerOfTwo(n)
print(ketqua)