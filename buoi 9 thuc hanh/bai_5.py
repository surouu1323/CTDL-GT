def perfect(n):
    numb = 0
    for i in range(1, n):
        if (n % i == 0):
            numb = numb +i
    if numb < n: 
        print(n,"la so deficient")
    else:
        print(n,"la so perfect")


n = int(input("Nhập số n: "))

if n <= 0:
    print("Nhập lại số nguyên dương.")
else:
    perfect(n)
    