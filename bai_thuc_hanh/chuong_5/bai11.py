class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def BSTTuanTu(self):
        return self._BSTTuanTu(self.root)

    def _BSTTuanTu(self, node):
        if node is None:
            return True

        is_left_child_only = node.left and node.right is None
        is_right_child_only = node.right and node.left is None

        if is_left_child_only or is_right_child_only:
            return True

        return self._BSTTuanTu(node.left) and self._BSTTuanTu(node.right)

# Tạo một cây nhị phân
tree = BinaryTree()

# Xây dựng cây nhị phân
tree.root = Node(4)
tree.root.left = Node(2)
tree.root.right = Node(6)
tree.root.left.left = Node(1)
tree.root.right.right = Node(8)

# Kiểm tra cây nhị phân có thỏa mãn tính chất của cây BST và tìm kiếm tuần tự hay không
is_bst_tuantu = tree.BSTTuanTu()

# In kết quả
if is_bst_tuantu:
    print("Cây nhị phân thỏa mãn tính chất của cây BST và tìm kiếm tuần tự")
else:
    print("Cây nhị phân không thỏa mãn tính chất của cây BST và tìm kiếm tuần tự")