def fibonacci_no_recursion(n):
    fib = [0, 1]
    if n <= 1:
        return fib[n]
    else:
        for i in range(2, n+1):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n]


n = int(input("Nhập số Fibonacci: "))

if n <= 0:
    print("Nhập lại số nguyên dương.")
else:
    print("Số Fibonacci tương ứng:", fibonacci_no_recursion(n))
