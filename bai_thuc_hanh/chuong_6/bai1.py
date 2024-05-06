class PhuongThuc:
    def __init__ (self,arr):
        self.arr = arr
    def Duynhat(self):
        numbers = list(set(self.arr))  # Lấy danh sách các số duy nhất từ mảng a
        numbers.sort()  # Sắp xếp các số duy nhất theo thứ tự tăng dần
        return numbers

a = PhuongThuc([1, 5, 3, 7, 5, 9, 7])

b = a.Duynhat()
print(a)
print(b)