class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

    def KiemTraBST(self, node):
        # Gọi phương thức _KiemTraBST() để kiểm tra xem cây có phải là một cây BST hay không
        is_bst = self._KiemTraBST(node)
        if is_bst:
            print("Cây là một cây BST")
        else:
            print("Cây không phải là cây BST")

    def _KiemTraBST(self, node):
        if node is None: # Nếu nút hiện tại là None thì trả về True
            return True
        
        elif node.left is None or node.right is None: # Nếu một trong các nút con (trái hoặc phải) là None thì trả về True
            return True
        
        # Nếu giá trị của nút con trái lớn hơn hoặc bằng giá trị của nút hiện tại thì trả về False
        # Nếu giá trị của nút con phải nhỏ hơn hoặc bằng giá trị của nút hiện tại thì trả về False
        elif node.left.info >= node.info or node.info >= node.right.info:
            return False
           
        # Kiểm tra xem cả hai cây con cũng phải là cây BST     
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
