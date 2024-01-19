
# The buffer_info() function is used to get the memory address and the length of the buffer that holds the array’s contents.



from array import array


arr1 = array("i", [1, 2, 3])

print (arr1)
print (arr1.buffer_info())
