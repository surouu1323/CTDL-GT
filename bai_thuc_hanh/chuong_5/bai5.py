class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def KiemTraBST(self, node):
        return self._KiemTraBST(node, float('-inf'), float('inf'))

    def _KiemTraBST(self, node, min_val, max_val):
        if node is None:
            return True

        if node.info <= min_val or node.info >= max_val:
            return False

        return (
            self._KiemTraBST(node.left, min_val, node.info) and
            self._KiemTraBST(node.right, node.info, max_val)
        )

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

# Gọi phương thức KiemTraBST() để kiểm tra xem cây có phải là BST hay không
is_bst = tree.KiemTraBST(tree.root)

# In kết quả
if is_bst:
    print("Cây là một cây BST")
else:
    print("Cây không phải là cây BST")