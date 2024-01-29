def printPairs(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            print(str(lst[i]) + "," + str(lst[j]))
            
my_list = [1, 2, 3, 4, 5, 6]
printPairs(my_list)