class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def KiemTraAVL(self, node):
        return self._KiemTraAVL(node) != -1

    def _KiemTraAVL(self, node):
        if node is None:
            return 0

        left_height = self._KiemTraAVL(node.left)
        if left_height == -1:
            return -1

        right_height = self._KiemTraAVL(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

# Tạo một cây nhị phân
tree = BinaryTree()

# Xây dựng cây nhị phân
tree.root = Node(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.left.right = Node(3)
tree.root.right.left = Node(5)
tree.root.right.right = Node(7)

# Gọi phương thức KiemTraAVL() để kiểm tra xem cây có phải là cây AVL hay không
is_avl = tree.KiemTraAVL(tree.root)

# In kết quả
if is_avl:
    print("Cây là một cây AVL")
else:
    print("Cây không phải là cây AVL")