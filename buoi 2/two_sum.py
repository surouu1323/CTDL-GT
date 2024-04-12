import array as arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
target = int(input("target: "))
x = len(l)
state = 0
print("Initial Array: ")
for i in range(1,x):
    for j in range(i+1,x):
        if (l[i]+l[j]) == target:
            print(l[i], end=" ")
            print(l[j],"\n")
            state = 1
if state == 0:
    print("Không có số thỏa điều kiện ")