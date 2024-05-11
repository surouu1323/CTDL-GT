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
                muc_tu.loai_tu,
                muc_tu.nghia,
                muc_tu.vi_du
            )
    
    def find(self, muc_tu):
        found_muc_tu = self._find_recursive(self.root, muc_tu)
    
        if found_muc_tu:
            print("Mục từ tìm thấy:")
            found_muc_tu.xem_muc_tu()
        else:
            print("Mục từ không tìm thấy.")
    
    def _find_recursive(self, node, muc_tu):
        if not node:
            return None
        if muc_tu == node.info.muc_tu:
            return node.info
        elif muc_tu < node.info.muc_tu:
            return self._find_recursive(node.left, muc_tu)
        else:
            return self._find_recursive(node.right, muc_tu)
        
        
    def delete(self, muc_tu):
        self.root = self._delete_recursive(self.root, muc_tu)

    def _delete_recursive(self, node, muc_tu):
        if not node:
            return None

        if muc_tu < node.info.muc_tu:
            node.left = self._delete_recursive(node.left, muc_tu)
        elif muc_tu > node.info.muc_tu:
            node.right = self._delete_recursive(node.right, muc_tu)
        else:
            # Nếu nút cần xóa được tìm thấy
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Trường hợp có hai con, tìm nút nhỏ nhất bên phải
            min_larger_node = self._find_min(node.right)
            node.info = min_larger_node.info
            node.right = self._delete_recursive(node.right, min_larger_node.info.muc_tu)

        return node
    
    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self):
        # Duyệt cây theo thứ tự inorder
        results = []
        self._inorder_recursive(self.root, results)
        return results

    def _inorder_recursive(self, node, results):
        if node:
            self._inorder_recursive(node.left, results)
            results.append(node.info)
            self._inorder_recursive(node.right, results)

class Hash:
    def __init__(self):
      # Bảng băm có 26 ô cho các ký tự từ 'a' đến 'z'
        self.table = {chr(i):[None] for i in range(ord('a'), ord('z')+1)}
        
    def __hash_func(self, word):
        # Hàm băm lấy ký tự đầu tiên
        return word[0].lower() # Đảm bảo xử lý chữ hoa chữ thường  
    
    def NhapTu(self, muc_tu, td):        
        # Tính vị trí trong bảng băm
        ky_tu_dau = self.__hash_func(muc_tu)
        bucket = self.table[ky_tu_dau]
        
        if any(elem is None for elem in bucket) :
            # Tạo một từ điển cho từ này
            word_info = {
                'ky_tu_dau' : ky_tu_dau,
                'cay_bst' : BST(),  # Tạo một BST mới nếu chưa tồn tại
            }
            cay_bst = word_info['cay_bst']
            cay_bst.insert(td)
            self.table[ky_tu_dau] = word_info
        else:
            # cay_bst = self.table[ky_tu_dau].get('cay_bst',0).insert(td)
            

        
    def TraTu(self, muc_tu):
        # Tìm từ trong bảng băm
        ky_tu_dau = self.__hash_func(muc_tu)
        
        # Nếu từ trong danh sách 
        if self.table[ky_tu_dau].get("ky_tu_dau",0) == ky_tu_dau:
            return self.table[ky_tu_dau].get('cay_bst',0)
        else:
            return None

dictionary = Hash()
file_name = "N21DCDT083_bam.json"
    
td = MucTu('a')
td.them_muc_tu('b', 'c', 'd')
dictionary.NhapTu('a', td)

td = MucTu('a')
td.them_muc_tu('e', 'f', 'g')
dictionary.NhapTu('a', td)
    

bst = dictionary.TraTu('a')
if bst is None:
    print ("Không có từ cần tìm kiếm")  # Nếu không tìm thấy từ
else:
    bst.find('a')
