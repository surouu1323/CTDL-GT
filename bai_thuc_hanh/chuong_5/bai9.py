class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def CayCon(self, other_tree):
        return self._CayCon(self.root, other_tree.root)

    def _CayCon(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        if node1 is None and node2 is not None:
            return False

        if node1 is not None and node2 is None:
            return True

        if node1.info != node2.info:
            return False

        left_result = self._CayCon(node1.left, node2.left)
        right_result = self._CayCon(node1.right, node2.right)

        return left_result or right_result

# Tạo hai cây nhị phân
tree1 = BinaryTree()
tree2 = BinaryTree()

# Xây dựng cây nhị phân thứ nhất
tree1.root = Node(1)
tree1.root.left = Node(2)
tree1.root.right = Node(3)
tree1.root.left.left = Node(4)
tree1.root.left.right = Node(5)

# Xây dựng cây nhị phân thứ hai
tree2.root = Node(2)
tree2.root.left = Node(4)
tree2.root.right = Node(5)

# Kiểm tra cây nhị phân thứ hai có là cây con của cây nhị phân thứ nhất hay không
is_subtree = tree1.CayCon(tree2)

# In kết quả
if is_subtree:
    print("Cây nhị phân thứ hai là cây con của cây nhị phân thứ nhất")
else:
    print("Cây nhị phân thứ hai không là cây con của cây nhị phân thứ nhất")