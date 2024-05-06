class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class PhuongThuc:
    def __init__(self):
        self.root = None

    def KiemTraBST(self, node):
        is_bst = self._KiemTraBST(node)
        if is_bst:
            print("Cây là một cây BST")
        else:
            print("Cây không phải là cây BST")

    def _KiemTraBST(self, node):
        if node is None: # If the current node is null then return true
            return True
        
        elif node.left is None or node.right is None: # If the value of the left child or right child is null then return true
            return True
        
        #If the value of the left child of the node is greater than or equal to the current node then return false
        #If the value of the right child of the node is less than or equal to the current node then return false
        elif node.left.info >= node.info or node.info >= node.right.info:
            return False
                
        return (
            self._KiemTraBST(node.left) and
            self._KiemTraBST(node.right)
        )

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

# Gọi phương thức KiemTraBST() để kiểm tra xem cây có phải là BST hay không
cay.KiemTraBST(cay.root)

cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)

cay.KiemTraBST(cay.root)
