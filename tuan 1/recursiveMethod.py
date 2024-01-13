def recursiveMethod(n):
    if n<1:
        print("n nho hon 1")
    else:
        recursiveMethod(n-1)
        print(n)

numDolls = int(input("nhap n: "))
recursiveMethod(numDolls)
