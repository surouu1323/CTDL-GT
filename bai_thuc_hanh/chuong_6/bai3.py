class PhuongThuc:
    def __init__ (self,arr):
        self.arr = arr
    def Giao(self, b):
        set_a = set(self.arr)  # Tạo tập hợp từ mảng a
        set_b = set(b)  # Tạo tập hợp từ mảng b
        intersection = set_a.intersection(set_b)  # Lấy giao của hai tập hợp
        sorted_intersection = sorted(intersection)  # Sắp xếp kết quả theo thứ tự tăng dần
        return sorted_intersection

a = PhuongThuc([1, 5, 3, 7, 9, 4, 2])
b = [9, 6, 2, 3, 8]
c = a.Giao(b)
print(c)