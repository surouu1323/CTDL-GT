class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

    def SoNut(self, node):
        if node is None: # Nếu node là None, trả về 0 (cây rỗng hoặc đã đến cuối nhánh).
            return 0
        else:
            #  Gọi đệ quy SoNut cho nút con bên trái (node.left) và nút con bên phải (node.right). 
            left_count = self.SoNut(node.left)
            right_count = self.SoNut(node.right)
            return left_count + right_count + 1 # Tổng số nút là tổng của nút bên trái, nút bên phải và chính nút hiện tại (+ 1).

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.left.left = Node(6)
cay.root.left.right = Node(5)
# cấu  trúc cây        
#        1
#      /   \
#     2     3
#    / \
#   4   5
#  /
# 6


# Gọi phương thức SoNut() để đếm số nút
so_nut = cay.SoNut(cay.root)

print("Số nút của cây là:", so_nut) # Kết quả sẽ là 6