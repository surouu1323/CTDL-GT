class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

    def CayCon(self, other_tree):
    # Kiểm tra nếu cây other_tree là cây con của cây hiện tại
        if self._CayCon(self.root, other_tree.root):
            print("Cây nhị phân thứ hai là cây con của cây nhị phân thứ nhất")
        else:
            print("Cây nhị phân thứ hai không là cây con của cây nhị phân thứ nhất")

    def _CayCon(self, node1, node2):
        # Nếu cả hai node đều là None, điều này có nghĩa là cả hai cây đều đã kết thúc tại đây và chúng là giống nhau
        if node1 is None and node2 is None:
            return True

        # Nếu node1 là None nhưng node2 không phải là None, điều này có nghĩa là other_tree lớn hơn hoặc khác nhau
        if node1 is None and node2 is not None:
            return False

        # Nếu node1 không phải là None nhưng node2 là None, điều này có nghĩa là cây hiện tại chứa other_tree như là cây con
        if node1 is not None and node2 is None:
            return True

        # Nếu thông tin của node hiện tại của cả hai cây không giống nhau, chúng không thể là cây con
        if node1.info != node2.info:
            return False

        # Kiểm tra đệ quy cho cây con bên trái và bên phải
        left_result = self._CayCon(node1.left, node2.left)
        right_result = self._CayCon(node1.right, node2.right)

        # Trả về kết quả kiểm tra của cây con bên trái hoặc bên phải
        return left_result or right_result

# Tạo hai cây nhị phân
cay1 = PhuongThuc()
cay2 = PhuongThuc()

# Xây dựng cây nhị phân thứ nhất
cay1.root = Node(1)
cay1.root.left = Node(2)
cay1.root.right = Node(3)
cay1.root.left.left = Node(4)
cay1.root.left.right = Node(5)

# Xây dựng cây nhị phân thứ hai
cay2.root = Node(2)
cay2.root.left = Node(4)
cay2.root.right = Node(5)

# Kiểm tra cây nhị phân thứ hai có là cây con của cây nhị phân thứ nhất hay không
is_subtree = cay1.CayCon(cay2)

# In kết quả
