class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

    def SoSanh(self, other_tree):
        # Gọi phương thức _SoSanh để so sánh hai cây từ gốc của chúng
        if self._SoSanh(self.root, other_tree.root):
            print("Hai cây nhị phân giống hệt nhau")
        else:
            print("Hai cây nhị phân không giống hệt nhau")

    def _SoSanh(self, node1, node2):
        # Nếu cả hai nút đều là None, nghĩa là chúng đều là cây con rỗng và giống hệt nhau
        if node1 is None and node2 is None:
            return True

        # Nếu chỉ một trong hai nút là None, nghĩa là cấu trúc cây khác nhau
        elif node1 is None or node2 is None:
            return False

        # Nếu giá trị của hai nút khác nhau, nghĩa là chúng không giống hệt nhau
        elif node1.info != node2.info:
            return False
        else:
            # Gọi đệ quy để so sánh cây con bên trái và bên phải
            left_result = self._SoSanh(node1.left, node2.left)
            right_result = self._SoSanh(node1.right, node2.right)

            # Trả về True nếu cả cây con bên trái và bên phải đều giống hệt nhau
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
