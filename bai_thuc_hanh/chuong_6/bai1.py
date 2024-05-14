class PhuongThuc:
    def __init__ (self, arr):
        self.arr = arr  # Gán mảng đầu vào cho thuộc tính arr của lớp

    def Duynhat(self):
        # Lấy danh sách các số duy nhất từ mảng arr bằng cách sử dụng set (loại bỏ các phần tử trùng lặp)
        numbers = list(set(self.arr))
        # Sắp xếp các số duy nhất theo thứ tự tăng dần
        numbers.sort()
        # Trả về danh sách các số duy nhất đã được sắp xếp
        return numbers

# Tạo một đối tượng PhuongThuc với mảng đầu vào là [1, 5, 3, 7, 5, 9, 7]
a = PhuongThuc([1, 5, 3, 7, 5, 9, 7])

# Gọi phương thức Duynhat() để lấy danh sách các số duy nhất đã được sắp xếp
b = a.Duynhat()

# In đối tượng a (sẽ hiển thị thông tin về đối tượng, không phải nội dung mảng)
print(a)

# In danh sách các số duy nhất đã được sắp xếp
print(b)
