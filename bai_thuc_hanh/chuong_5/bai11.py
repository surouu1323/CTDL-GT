class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class PhuongThuc:
    def __init__(self):
        self.root = None

    def BSTTuanTu(self):
        if self._BSTTuanTu(self.root):
            print("Cây nhị phân thỏa mãn tính chất của cây BST và tìm kiếm tuần tự")
        else:
            print("Cây nhị phân không thỏa mãn tính chất của cây BST và tìm kiếm tuần tự")

    def _BSTTuanTu(self, node):
        if node is None:
            return True

        if node.left and node.right is not None:
            return False

        return self._BSTTuanTu(node.left) and self._BSTTuanTu(node.right)

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.root = Node(4)
cay.root.left = Node(2)
cay.root.left.left = Node(1)

# Kiểm tra cây nhị phân có thỏa mãn tính chất của cây BST và tìm kiếm tuần tự hay không
is_bst_tuantu = cay.BSTTuanTu()
