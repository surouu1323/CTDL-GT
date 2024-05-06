class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class PhuongThuc:
    def __init__(self):
        self.root = None

    def SoNut(self, node):
        if node is None:
            return 0
        else:
            left_count = self.SoNut(node.left)
            right_count = self.SoNut(node.right)
            return left_count + right_count + 1

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.left.left = Node(6)
cay.root.left.right = Node(5)

# Gọi phương thức SoNut() để đếm số nút
so_nut = cay.SoNut(cay.root)

print("Số nút của cây là:", so_nut)
print(cay.root.right.info)