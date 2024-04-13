class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class BinaryTree:
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
tree = BinaryTree()

# Xây dựng cây nhị phân
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Sao chép cây nhị phân
copied_tree = tree.Chep()

# In cây nhị phân ban đầu
print("Cây nhị phân ban đầu:")
# Gọi phương thức inOrder để in cây nhị phân
def inOrder(node):
    if node is not None:
        inOrder(node.left)
        print(node.info, end=" ")
        inOrder(node.right)
inOrder(tree.root)
print()

# In cây nhị phân đã sao chép
print("Cây nhị phân đã sao chép:")
inOrder(copied_tree)