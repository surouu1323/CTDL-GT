def square (numbers):
    for n in numbers:
        yield n ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = square(numbers)

print(squared_numbers)