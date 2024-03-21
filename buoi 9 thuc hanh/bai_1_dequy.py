def fibonacci_recursion(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

n = int(input("Nhập số Fibonacci: "))

if n <= 0:
    print("Nhập lại số nguyên dương.")
else:
    print("Số Fibonacci tương ứng:", fibonacci_recursion(n))