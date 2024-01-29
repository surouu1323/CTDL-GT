def reverse(lst):
    n = len(lst)
    for i in range(n // 2):
        other = n - i - 1
        lst[i], lst[other] = lst[other], lst[i]

    print(lst)

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
reverse(my_list)