def recursiveMethod(n):
    if n<1:
        print("n nho hon 1")
    else:
        recursiveMethod(n-1)
        print(n)

n = int(input("nhap n: "))
recursiveMethod(n)
