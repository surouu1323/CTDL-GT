def foo(lst):
    total_sum = sum(lst)
    total_product = 1

    for i in lst:
        total_product *= i

    print("Sum =", total_sum, ", Product =", total_product)

my_list = [2, 3, 4, 5, 6, 7]
foo(my_list)