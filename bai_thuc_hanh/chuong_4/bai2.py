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

    def DaoNguoc(self):
        stack = []
        current = self.Head
        while current is not None:
            stack.append(current)
            current = current.Next
        self.Head = stack.pop()
        current = self.Head
        while stack:
            current.Next = stack.pop()
            current = current.Next
        current.Next = None

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

# Đảo ngược danh sách liên kết
dslk.DaoNguoc()

# In danh sách liên kết sau khi đảo ngược
print("Danh sách liên kết sau khi đảo ngược:")
dslk.InDanhSach()