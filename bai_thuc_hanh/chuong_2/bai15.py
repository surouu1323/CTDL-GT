class PhuongThuc:
    def __init__(self, arr):
        self.arr = arr  # Khởi tạo một đối tượng PhuongThuc với một thuộc tính là một mảng arr.
        
    def DayConDaiNhat(self, b):
        c = []  # Mảng chứa dãy con có chiều dài lớn nhất
        a = self.arr
        for i in range(len(a)):
            for j in range(len(b)): # lặp qua từng phần tử i trong mảng arr và từng phần tử j trong mảng b.
                
                if a[i] == b[j]: # Nếu a[i] =  b[j], bắt đầu kiểm tra dãy con từ vị trí hiện tại trong arr.
                    current_c = [a[i]]
                    k = 1

                    while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                        # điều kiện i + k < len(a) và j + k < len(b) tức là không vượt qua phạm vi của mảng
                        #  so sánh các phần tử a[i + k] và b[j + k]
                        current_c.append(a[i + k]) #  mở rộng dãy current_c bằng cách thêm phần tử a[i + k]
                        k += 1

                    if len(current_c) > len(c): # so sánh chiều dài của dãy current_c này với dãy có length nhất (c). 
                        c = current_c # Nếu dãy mới dài hơn, chúng ta cập nhật c bằng dãy mới này.
        return c
    
a = PhuongThuc([1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5])
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
print(a.DayConDaiNhat(b))