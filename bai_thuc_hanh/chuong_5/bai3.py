class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
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
tree = BinaryTree()

# Xây dựng cây nhị phân
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)

# Gọi phương thức SoNutLa() để đếm số nút lá
so_nut_la = tree.SoNutLa(tree.root)

print("Số nút lá của cây là:", so_nut_la)