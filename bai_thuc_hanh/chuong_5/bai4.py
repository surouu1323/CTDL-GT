class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

    def SoNutTrungGian(self, node):
        if node is None: # Nếu node là None, tức là cây con này không tồn tại hoặc đã đến lá, phương thức trả về 0.
            return 0
        # Nếu node không phải là None, nhưng cả hai node.left và node.right đều là None, 
        # tức là node là một nút lá, phương thức cũng trả về 0 vì nút lá không được tính là nút trung gian.
        elif node.left is None and node.right is None:  
            return 0
        else:
            #  Nếu node không phải là nút lá, phương thức tiến hành đệ quy để đếm số nút trung gian của cây con trái và cây con phải.
            left_count = self.SoNutTrungGian(node.left)
            right_count = self.SoNutTrungGian(node.right)
            return left_count + right_count + 1

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)


# Gọi phương thức SoNutTrungGian() để đếm số nút trung gian
so_nut_trung_gian = cay.SoNutTrungGian(cay.root)

print("Số nút trung gian của cây là:", so_nut_trung_gian)