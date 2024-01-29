def printUnorderedPairs(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            print(f"{lst[i]},{lst[j]}")

my_list = [1, 2, 3, 4, 5]
printUnorderedPairs(my_list)