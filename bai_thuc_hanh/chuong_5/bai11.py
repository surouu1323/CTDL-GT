class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

    def BSTTuanTu(self):
        # Gọi phương thức _BSTTuanTu() với node gốc (self.root)
        if self._BSTTuanTu(self.root):
            # Nếu kết quả trả về True, in ra thông báo cây nhị phân thỏa mãn tính chất của cây BST và tìm kiếm tuần tự
            print("Cây nhị phân thỏa mãn tính chất của cây BST và tìm kiếm tuần tự")
        else:
            # Nếu kết quả trả về False, in ra thông bá
            # o cây nhị phân không thỏa mãn tính chất của cây BST và tìm kiếm tuần tự
            print("Cây nhị phân không thỏa mãn tính chất của cây BST và tìm kiếm tuần tự")

    def _BSTTuanTu(self, node):
        # Nếu node hiện tại là None (đã duyệt hết cây hoặc cây rỗng), trả về True
        if node is None:
            return True

        # Nếu node có cả con trái và con phải không phải là None (tức là node có cả 2 con), trả về False
        if node.left and node.right is not None:
            return False

        # Gọi đệ quy để kiểm tra cây con bên trái và cây con bên phải
        return self._BSTTuanTu(node.left) and self._BSTTuanTu(node.right)


# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.root = Node(4)
cay.root.left = Node(2)
cay.root.left.left = Node(1)

# Kiểm tra cây nhị phân có thỏa mãn tính chất của cây BST và tìm kiếm tuần tự hay không
is_bst_tuantu = cay.BSTTuanTu()
