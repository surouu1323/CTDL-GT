class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def ChieuCao(self, node):
        if node is None:
            return 0
        else:
            left_height = self.ChieuCao(node.left)
            right_height = self.ChieuCao(node.right)
            return max(left_height, right_height) + 1

# Tạo một cây nhị phân
tree = BinaryTree()

# Xây dựng cây nhị phân
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Gọi phương thức ChieuCao() để tính chiều cao
chieu_cao = tree.ChieuCao(tree.root)

print("Chiều cao của cây là:", chieu_cao)