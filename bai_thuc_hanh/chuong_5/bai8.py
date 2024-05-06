class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class PhuongThuc:
    def __init__(self):
        self.root = None

    def SoSanh(self, other_tree):
        if self._SoSanh(self.root, other_tree.root):
            print("Hai cây nhị phân giống hệt nhau")
        else:
            print("Hai cây nhị phân không giống hệt nhau")

    def _SoSanh(self, node1, node2):
        if node1 is None and node2 is None:
            return True

        elif node1 is None or node2 is None:
            return False

        elif node1.info != node2.info:
            return False
        else:
            left_result = self._SoSanh(node1.left, node2.left)
            right_result = self._SoSanh(node1.right, node2.right)

            return left_result and right_result

# Tạo hai cây nhị phân
cay1 = PhuongThuc()
cay2 = PhuongThuc()

# Cây nhị phân thứ nhất
cay1.root = Node(1)
cay1.root.left = Node(2)
cay1.root.right = Node(3)

# Cây nhị phân thứ hai
cay2.root = Node(1)
cay2.root.left = Node(2)
cay2.root.right = Node(3)

# So sánh hai cây nhị phân
cay1.SoSanh(cay2)
