class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
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
tree = BinaryTree()

# Xây dựng cây nhị phân
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Gọi phương thức SoNut() để đếm số nút
so_nut = tree.SoNut(tree.root)

print("Số nút của cây là:", so_nut)