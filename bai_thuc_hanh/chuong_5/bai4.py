class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

class PhuongThuc:
    def __init__(self):
        self.root = None

    def SoNutTrungGian(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:  # Kiểm tra nút lá
            return 0
        else:
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