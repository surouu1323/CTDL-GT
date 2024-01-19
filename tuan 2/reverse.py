
import array as arr
a = [1, 3, 5, 7, 9]

def reverse(array):
    for i in range(0, int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)
    
reverse(a)
