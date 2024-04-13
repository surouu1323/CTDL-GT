class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def SoSanh(self, other_tree):
        return self._SoSanh(self.root, other_tree.root)

    def _SoSanh(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False

        if node1.info != node2.info:
            return False

        left_result = self._SoSanh(node1.left, node2.left)
        right_result = self._SoSanh(node1.right, node2.right)

        return left_result and right_result

# Tạo hai cây nhị phân
tree1 = BinaryTree()
tree2 = BinaryTree()

# Xây dựng cây nhị phân thứ nhất
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)

# Xây dựng cây nhị phân thứ hai
tree2.root = Node(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)

# So sánh hai cây nhị phân
is_same = tree1.SoSanh(tree2)

# In kết quả
if is_same:
    print("Hai cây nhị phân giống hệt nhau")
else:
    print("Hai cây nhị phân không giống hệt nhau")