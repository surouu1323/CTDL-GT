class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

def KiemTraAVL(self, node):
    # Gọi phương thức _KiemTraAVL() và kiểm tra xem kết quả khác -1 hay không
    return self._KiemTraAVL(node) != -1

def _KiemTraAVL(self, node):
    # Nếu nút hiện tại là None thì trả về 0 (chiều cao của cây con là 0)
    if node is None:
        return 0

    # Gọi đệ quy để kiểm tra chiều cao của cây con bên trái
    left_height = self._KiemTraAVL(node.left)
    # Nếu chiều cao của cây con bên trái là -1 thì trả về -1 (cây không cân bằng)
    if left_height == -1:
        return -1

    # Gọi đệ quy để kiểm tra chiều cao của cây con bên phải
    right_height = self._KiemTraAVL(node.right)
    # Nếu chiều cao của cây con bên phải là -1 thì trả về -1 (cây không cân bằng)
    if right_height == -1:
        return -1

    # Nếu sự chênh lệch giữa chiều cao của cây con bên trái và bên phải lớn hơn 1 thì trả về -1 (cây không cân bằng)
    if abs(left_height - right_height) > 1:
        return -1

    # Trả về chiều cao lớn nhất của cây con và cộng thêm 1 (tính cả nút hiện tại)
    return max(left_height, right_height) + 1


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

# Gọi phương thức KiemTraAVL() để kiểm tra xem cây có phải là cây AVL hay không
is_avl = cay.KiemTraAVL(cay.root)

# In kết quả
if is_avl:
    print("Cây là một cây AVL")
else:
    print("Cây không phải là cây AVL")