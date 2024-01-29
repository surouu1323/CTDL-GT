def factorial(n):
    # n < 0
    if n < 0:
        return -1
    # 0! = 1
    elif n == 0:
        return 1
    # n > 0
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

result = factorial(6)
print(f"The factorial of 6 is: {result}")