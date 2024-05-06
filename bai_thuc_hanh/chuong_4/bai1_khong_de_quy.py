class Node:
    def __init__(self, info):
        self.Info = info
        self.Next = None

class PhuongThuc:
    def __init__(self):
        self.Head = None

    def Them(self, info):
        node = Node(info)
        if self.Head is None:
            self.Head = node
        else:
            current = self.Head
            while current.Next is not None:
                current = current.Next
            current.Next = node


    def InNguoc(self):
        stack = []
        current = self.Head
        while current is not None:
            stack.append(current.Info)
            current = current.Next
        while stack:
            print(stack.pop(), end=" ")

    def InDanhSach(self):
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

# In ngược danh sách liên kết bằng phương pháp không đệ qui
print("\nIn ngược danh sách (không đệ qui):")
dslk.InNguoc()