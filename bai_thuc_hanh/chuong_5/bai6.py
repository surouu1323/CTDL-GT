class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class PhuongThuc:
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
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.root = Node(4)
cay.root.left = Node(2)
cay.root.right = Node(6)
cay.root.left.left = Node(1)
cay.root.left.right = Node(3)
cay.root.right.left = Node(5)
cay.root.right.right = Node(7)

# Gọi phương thức KiemTraAVL() để kiểm tra xem cây có phải là cây AVL hay không
is_avl = cay.KiemTraAVL(cay.root)

# In kết quả
if is_avl:
    print("Cây là một cây AVL")
else:
    print("Cây không phải là cây AVL")