class Node:
    def __init__(self, data): # Lớp này đại diện cho một nút trong cây nhị phân.
        self.info = data # Chứa dữ liệu của nút.
        self.left = None # Trỏ đến nút con bên trái.
        self.right = None # Trỏ đến nút con bên phải.

class PhuongThuc: # Lớp này đại diện cho cây nhị phân và chứa các phương thức thao tác với cây.
    def __init__(self):
        self.root = None # Gốc của cây, ban đầu được khởi tạo là None.

    def ChieuCao(self, node):
        if node is None: # Nếu node là None, tức là cây con này không tồn tại hoặc đã đến lá
            return 0 # phương thức trả về 0, báo hiệu chiều cao là 0.

        else:
            left_height = self.ChieuCao(node.left) # Chiều cao của cây con bên trái được tính bằng cách gọi đệ quy ChieuCao(node.left).
            right_height = self.ChieuCao(node.right) # Chiều cao của cây con bên phải được tính bằng cách gọi đệ quy ChieuCao(node.right).
            # Chiều cao của cây tại node sẽ là chiều cao lớn nhất giữa chiều cao của cây con trái và cây con phải, 
            # cộng thêm 1 (để tính cả nút node hiện tại). 
            # Điều này được thực hiện bằng hàm max(left_height, right_height) + 1.
            return max(left_height, right_height) + 1

# Tạo một cây nhị phân
cay = PhuongThuc()

# Xây dựng cây nhị phân
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

# Gọi phương thức ChieuCao() để tính chiều cao
chieu_cao = cay.ChieuCao(cay.root)

print("Chiều cao của cây là:", chieu_cao)