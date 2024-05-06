class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class PhuongThuc:
    def __init__(self):
        self.root = None

    def Chep(self):
        
        return self._Chep(self.root)

    def _Chep(self, node):
        if node is None:
            return None

        new_node = Node(node.info)
        new_node.left = self._Chep(node.left)
        new_node.right = self._Chep(node.right)

        return new_node

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

# Sao chép cây nhị phân
copied_cay = cay.Chep()

# Dùng đệ quy để in cây BST
def inOrder(node):
    if node.left is None or node.right is None:
        print(node.info, end=" ")
    else:
        inOrder(node.left)
        inOrder(node.right)
        print(node.info, end=" ")

# In cây nhị phân ban đầu
print("Cây nhị phân ban đầu:")
inOrder(cay.root)
print()

# In cây nhị phân đã sao chép
print("Cây nhị phân đã sao chép:")
inOrder(copied_cay)