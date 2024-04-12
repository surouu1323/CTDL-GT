def DayConDaiNhat(a, b):
    c = []  # Mảng chứa dãy con có chiều dài lớn nhất

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                current_c = [a[i]]
                k = 1

                while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                    current_c.append(a[i + k])
                    k += 1

                if len(current_c) > len(c):
                    c = current_c

    return c
a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
print(DayConDaiNhat(a, b))  # Kết quả: [6, 2, 5, 3, 7, 9]