
import array as arr
a = [1, 3, 5, 7, 9]
b = [2, 4 ,6 ,8 ,10]

def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

printUnorderedPairs(a,b)