def fibonacci_no_recursion(n):
    fib = [1, 1]
    # Nếu n nhỏ hơn hoặc bằng 2 (n <= 2), hàm trả về giá trị fib[n-1]
    if n <= 2:
        return fib[n-1]
    # trường hợp n lớn hơn 2
    else:
        for i in range(2, n): # bắt đầu từ 2 (vì chúng ta đã có sẵn hai số Fibonacci đầu tiên) và kết thúc ở n.
            fib.append(fib[i-1] + fib[i-2])
            # Trong mỗi lần lặp, số Fibonacci tiếp theo được tính bằng cách cộng hai số Fibonacci gần nhất đã được tính trước đó 
            # và sau đó được thêm vào danh sách fib.
        return fib[n-1]


n = int(input("Nhập số Fibonacci: "))

if n <= 0:
    print("Nhập lại số nguyên dương.")
else:
    print("Số Fibonacci tương ứng:", fibonacci_no_recursion(n))
