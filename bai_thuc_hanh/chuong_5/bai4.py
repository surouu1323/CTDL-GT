class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:  # Kiểm tra nút lá
            return 0
        else:
            left_count = self.SoNutTrungGian(node.left)
            right_count = self.SoNutTrungGian(node.right)
            return left_count + right_count + 1

# Tạo một cây nhị phân
tree = BinaryTree()

# Xây dựng cây nhị phân
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)

# Gọi phương thức SoNutTrungGian() để đếm số nút trung gian
so_nut_trung_gian = tree.SoNutTrungGian(tree.root)

print("Số nút trung gian của cây là:", so_nut_trung_gian)