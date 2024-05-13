# Hàm factorial(i) tính giai thừa của một số nguyên i bằng cách sử dụng đệ quy.
def factorial(i):
    if i <=1:
        return 1
    else:
        return i * factorial(i-1)

# Hàm neper(n) tính xấp xỉ của số e bằng cách tính tổng ngược của các giai thừa nghịch đảo từ 1 đến n.
def neper(n):
    if n <= 1:
        return 2
    else:
        return 1/factorial(n) + neper(n-1)

n = int(input("Nhập số n: "))

if n <= 0:
    print("Nhập lại n")
else:
    print("Số e tuong ung:", neper(n))