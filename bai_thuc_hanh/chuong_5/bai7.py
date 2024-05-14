class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

    def Chep(self):
        # Gọi phương thức đệ quy _Chep() để sao chép cây nhị phân, bắt đầu từ nút gốc (self.root)
        return self._Chep(self.root)

    def _Chep(self, node):
        # Nếu nút hiện tại là None, trả về None (điểm dừng của đệ quy)
        if node is None:
            return None

        # Tạo một nút mới với thông tin của nút hiện tại
        new_node = Node(node.info)
        # Sao chép cây con bên trái của nút hiện tại và gán cho cây con bên trái của nút mới
        new_node.left = self._Chep(node.left)
        # Sao chép cây con bên phải của nút hiện tại và gán cho cây con bên phải của nút mới
        new_node.right = self._Chep(node.right)

        # Trả về nút mới đã được sao chép
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