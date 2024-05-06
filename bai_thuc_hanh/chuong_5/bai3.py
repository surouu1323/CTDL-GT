class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class PhuongThuc:
    def __init__(self):
        self.root = None

    def SoNutLa(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:  # Kiểm tra nút lá
            return 1
        else:
            left_count = self.SoNutLa(node.left)
            right_count = self.SoNutLa(node.right)
            return left_count + right_count

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)
cay.root.right.left = Node(6)

# Gọi phương thức SoNutLa() để đếm số nút lá
so_nut_la = cay.SoNutLa(cay.root)

print("Số nút lá của cây là:", so_nut_la)