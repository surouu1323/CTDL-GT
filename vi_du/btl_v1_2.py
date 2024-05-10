class Nghia:
    def __init__(self, loai_tu, nghia, vi_du):
        self.loai_tu = loai_tu
        self.nghia = nghia
        self.vi_du = vi_du
        self.next = None
        
    def __repr__(self):
        return f"({self.loai_tu}): {self.nghia}. Ví dụ: {self.vi_du}"
    
class MucTu:
    def __init__(self, muc_tu):
        self.head = None
        self.muc_tu = muc_tu
    
    def them_muc_tu(self, loai_tu, nghia, vi_du):
        new_nghia = Nghia(loai_tu, nghia, vi_du)
        # Chèn nghĩa vào danh sách theo thứ tự của 'loai_tu'
        if self.head is None or new_nghia.loai_tu > self.head.loai_tu:
            new_nghia.next = self.head
            self.head = new_nghia
        else:
            current = self.head
            while current.next and current.next.loai_tu < new_nghia.loai_tu:
                current = current.next
            new_nghia.next = current.next
            current.next = new_nghia
    
    def xem_muc_tu(self):
        # In danh sách liên kết các nghĩa
        current = self.head
        while current:
            print(current)
            current = current.next

class BSTNode:
    def __init__(self, muc_tu):
        self.info = muc_tu
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, muc_tu):
        if not self.root:
            self.root = BSTNode(muc_tu)
        else:
            self._insert_recursive(self.root, muc_tu)
            
    def _insert_recursive(self, node, muc_tu):
        if muc_tu.muc_tu < node.info.muc_tu:
            if not node.left:
                node.left = BSTNode(muc_tu)
            else:
                self._insert_recursive(node.left, muc_tu)
        elif muc_tu.muc_tu > node.info.muc_tu:
            if not node.right:
                node.right = BSTNode(muc_tu)
            else:
                self._insert_recursive(node.right, muc_tu)
        else:
            # Nếu mục từ đã tồn tại, thêm nghĩa vào mục từ
            node.info.them_muc_tu(
                muc_tu.head.loai_tu,
                muc_tu.head.nghia,
                muc_tu.head.vi_du
            )
    
    def find(self, muc_tu):
        return self._find_recursive(self.root, muc_tu)
    
    def _find_recursive(self, node, muc_tu):
        if not node:
            return None
        if muc_tu == node.info.muc_tu:
            return node.info
        elif muc_tu < node.info.muc_tu:
            return self._find_recursive(node.left, muc_tu)
        else:
            return self._find_recursive(node.right, muc_tu)


# Tạo cây BST
bst_dictionary = BST()

# Tạo mục từ và thêm vào BST
td = MucTu('muc_tu')
td.them_muc_tu('n', 'nang', 'vua')
td.them_muc_tu('adj', 'map', 'vua')
td.them_muc_tu('adj', 'thap', 'vua')

# Chèn mục từ vào BST
bst_dictionary.insert(td)

# Tìm và in mục từ từ BST
found_muc_tu = bst_dictionary.find('muc_tu')
if found_muc_tu:
    print("Mục từ tìm thấy:")
    found_muc_tu.xem_muc_tu()
else:
    print("Mục từ không tìm thấy.")
