class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

    def CanBangHoanToan(self):
        # Phương thức này được gọi từ bên ngoài và kiểm tra xem cây nhị phân có cân bằng hoàn toàn hay không.
        # Nó bắt đầu kiểm tra từ gốc của cây.
        return self._CanBangHoanToan(self.root)

    def _CanBangHoanToan(self, node):
        # Phương thức đệ quy để kiểm tra xem cây nhị phân con có cân bằng hoàn toàn hay không.
        if node is None:
            # Nếu nút hiện tại là None, nghĩa là cây con này không tồn tại và do đó được xem là cân bằng.
            return True

        # Đếm số nút trong cây con bên trái.
        left_subtree_count = self._DemNut(node.left)
        # Đếm số nút trong cây con bên phải.
        right_subtree_count = self._DemNut(node.right)

        # Kiểm tra sự chênh lệch số lượng nút giữa cây con bên trái và bên phải.
        if abs(left_subtree_count - right_subtree_count) > 1:
            # Nếu sự chênh lệch lớn hơn 1, cây không cân bằng hoàn toàn.
            return False

        # Tiếp tục kiểm tra đệ quy cho cây con bên trái và bên phải.
        return self._CanBangHoanToan(node.left) and self._CanBangHoanToan(node.right)

    def _DemNut(self, node):
        # Phương thức đệ quy để đếm tổng số nút trong cây con.
        if node is None:
            # Nếu nút hiện tại là None, trả về 0 vì không có nút nào ở cây con này.
            return 0

        # Đếm nút hiện tại (1) cộng với tổng số nút trong cây con bên trái và cây con bên phải.
        return 1 + self._DemNut(node.left) + self._DemNut(node.right)


# Tạo một cây nhị phân
tree = PhuongThuc()

# Xây dựng cây nhị phân
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# Kiểm tra cây nhị phân có cân bằng hoàn toàn hay không
is_balanced = tree.CanBangHoanToan()

# In kết quả
if is_balanced:
    print("Cây nhị phân là cây cân bằng hoàn toàn")
else:
    print("Cây nhị phân không là cây cân bằng hoàn toàn")