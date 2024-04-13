class DanhSachLienKet:
    def __init__(self):
        self.Head = None

    def ThemPhanTu(self, info):
        node = Node(info)
        if self.Head is None:
            self.Head = node
        else:
            current = self.Head
            while current.Next is not None:
                current = current.Next
            current.Next = node

    def InNguocDeQui(self, node):
        if node is None:
            return
        self.InNguocDeQui(node.Next)
        print(node.Info, end=" ")

    def InNguocKhongDeQui(self):
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


class Node:
    def __init__(self, info):
        self.Info = info
        self.Next = None


# Tạo danh sách liên kết
dslk = DanhSachLienKet()
dslk.ThemPhanTu(1)
dslk.ThemPhanTu(2)
dslk.ThemPhanTu(3)
dslk.ThemPhanTu(4)
dslk.ThemPhanTu(5)

# In danh sách liên kết
print("Danh sách liên kết:")
dslk.InDanhSach()

# In ngược danh sách liên kết bằng phương pháp đệ qui
print("In ngược danh sách (đệ qui):")
dslk.InNguocDeQui(dslk.Head)

# In ngược danh sách liên kết bằng phương pháp không đệ qui
print("\nIn ngược danh sách (không đệ qui):")
dslk.InNguocKhongDeQui()