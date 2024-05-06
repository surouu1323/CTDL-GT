class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class PhuongThuc:
    def __init__(self):
        self.root = None

    def CanBangHoanToan(self):
        return self._CanBangHoanToan(self.root)

    def _CanBangHoanToan(self, node):
        if node is None:
            return True

        left_subtree_count = self._DemNut(node.left)
        right_subtree_count = self._DemNut(node.right)

        if abs(left_subtree_count - right_subtree_count) > 1:
            return False

        return self._CanBangHoanToan(node.left) and self._CanBangHoanToan(node.right)

    def _DemNut(self, node):
        if node is None:
            return 0

        return 1 + self._DemNut(node.left) + self._DemNut(node.right)

# Tạo một cây nhị phân
tree = PhuongThuc()

# Xây dựng cây nhị phân
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Kiểm tra cây nhị phân có cân bằng hoàn toàn hay không
is_balanced = tree.CanBangHoanToan()

# In kết quả
if is_balanced:
    print("Cây nhị phân là cây cân bằng hoàn toàn")
else:
    print("Cây nhị phân không là cây cân bằng hoàn toàn")