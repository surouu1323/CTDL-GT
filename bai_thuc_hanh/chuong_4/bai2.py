class Node:
    def __init__(self, info): # khởi tạo với thông tin info và con trỏ Next trỏ đến None.
        self.Info = info
        self.Next = None

class PhuongThuc:
    def __init__(self):
        self.Head = None # khởi tạo với Head là None.

    def Them(self, info): # Thêm một Node mới vào cuối danh sác
        node = Node(info)
        if self.Head is None: # Nếu danh sách rỗng
            self.Head = node  # Head sẽ là Node mới
        else:
            current = self.Head
            while current.Next is not None: # duyệt đến cuối danh sách và thêm Node mới
                current = current.Next
            current.Next = node

    def DaoNguoc(self):
        stack = []  # Tạo một ngăn xếp để lưu trữ các phần tử.
        current = self.Head
        while current is not None: # Duyệt qua danh sách
            stack.append(current) # thêm các phần tử vào ngăn xếp.
            current = current.Next
            
        self.Head = stack.pop() # Lấy các nút ra khỏi ngăn xếp
        current = self.Head # lấy phần tử đầu tiên ra khỏi ngăn xếp làm nút đầu tiên
        while stack:
            current.Next = stack.pop() # lấy phần tử tiếp theo ra khỏi ngăn xếp làm nút tiếp theo
            current = current.Next  # liên kết các nút lại với nhau
        current.Next = None

    def InDanhSach(self): # In tất cả các phần tử trong danh sách theo thứ tự từ đầu đến cuối.
        current = self.Head
        while current is not None:
            print(current.Info, end=" ")
            current = current.Next
        print()


# Tạo danh sách liên kết
dslk = PhuongThuc()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)
dslk.Them(5)

# In danh sách liên kết
print("Danh sách liên kết:")
dslk.InDanhSach()

dslk.DaoNguoc()
# In ngược danh sách liên kết
print("In ngược danh sách :")
dslk.InDanhSach()
