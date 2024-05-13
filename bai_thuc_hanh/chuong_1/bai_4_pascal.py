# Hàm factorial(i) tính giai thừa của một số nguyên i bằng phương pháp đệ quy.
def factorial(i):
    if i <=1:
        return 1
    else:
        return i * factorial(i-1)
    
# Hàm ncr(n, r) tính giá trị của hệ số nhị thức C(n, r) , 
# là số cách chọn r phần tử từ n phần tử không phân biệt nhau. 
# Công thức tính như sau: C(n, r) = n! / (r! * (n-r)!).
def ncr(n, r):
    return int(factorial(n) / (factorial(n - r) * factorial(r)))
 
n = int(input("Nhập số n: "))

if n <= 0:
    print("Nhập lại n")
else:
    print("Ve tam giac Pascal:")
    # Vòng lặp ngoài chạy từ 1 đến n (bao gồm cả n).
    for i in range(1, n + 1):   
        print('n=',i, end=" ") 
        # Vòng lặp chạy từ 0 đến n, và tại mỗi vị trí (i, j), 
        # giá trị của hệ số nhị thức C(i, j) được tính bằng cách gọi hàm ncr(i, j).
        for j in range(0, n + 1):
            if(ncr(i, j) != 0):
                print(" {:<3}".format(ncr(i, j)), end="") # in ra với định dạng cố định là 3 ký tự và được căn trái
        print("")