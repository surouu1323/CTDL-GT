
import array as arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def printPairs(array):
    for i in array:
        for j in array:
            print(str(i)+","+str(j))
            
printPairs(l)