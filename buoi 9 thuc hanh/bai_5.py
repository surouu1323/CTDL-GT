def perfect(x,y):
    
    for n in range(x, y+1):
        numb = int(0)
        for i in range(1, n):
            if (n % i == 0):
                numb = numb + i        
        if numb < n: 
            print(n,"la so deficient")
        elif numb > n:
            print(n,"la so abundant")
        else:
            print(n,"la so perfect")


x = int(input("Nhập số x: "))
y = int(input("Nhập số y: "))

if x <= 0:
    print("Nhập lại x ")
elif y <= 0:
    print("Nhập lại x ")
else:
    perfect(x,y)
    
    
print("Nhập vào số N cần tìm ước: ")