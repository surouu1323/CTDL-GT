# deficient (số thiếu), abundant (số thặng), và perfect (số hoàn hảo) 
def perfect(x,y):
    for n in range(x, y+1): # Dùng một vòng lặp for để lặp qua tất cả các số từ x đến y
        numb = int(0)
        for i in range(1, n): # Trong mỗi vòng lặp, tính tổng các ước của số đó
            if (n % i == 0):
                numb = numb + i        
        if numb < n: # kiểm tra xem số đó có là deficient, abundant, hoặc perfect và in ra kết quả tương ứng
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