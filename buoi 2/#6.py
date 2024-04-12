
#The fromlist() function is simply used to append or add a list to the ending of a given array. 

import array as arr

x = arr.array('i', [1,2,3,4,5,6,7])

y = [8, 9, 10]


x.fromlist(y)

print(x)