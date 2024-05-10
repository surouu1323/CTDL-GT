class Nghia:
    def __init__ (self, loai_tu, nghia, vi_du):
        self.loai_tu = loai_tu
        self.nghia = nghia
        self.vi_du = vi_du
        self.next = None
        
    def __repr__ (self):
        return f"({self.loai_tu}): {self.nghia}. Ví dụ: {self.vi_du}"
    
        
class MucTu:
    def __init__ (self,muc_tu):
        self.head = None
        self.muc_tu = muc_tu
        
    # def them_muc_tu (self, loai_tu, nghia, vi_du):
    #     new_nghia = Nghia (loai_tu, nghia, vi_du)
    #     if self.head is None:
    #         self.head = new_nghia
    #         return
    #     else:
    #         last = self.head
    #         while last.next:
    #             if last.next.loai_tu < new_nghia.loai_tu:
    #                 temp = last.next
    #                 last.next = new_nghia   
    #                 new_nghia.next = temp
    #                 return
    #             last = last.next
                
    #         if last.loai_tu < new_nghia.loai_tu:
    #             temp = last
    #             self.head = new_nghia
    #             new_nghia.next = temp
    #         else:
    #             last.next = new_nghia
    
    def them_muc_tu(self, loai_tu, nghia, vi_du):
        new_nghia = Nghia(loai_tu, nghia, vi_du)
        # Chèn nghĩa mới vào đúng vị trí
        if self.head is None or self.head.loai_tu > new_nghia.loai_tu:
            new_nghia.next = self.head
            self.head = new_nghia
            return
        
        current = self.head
        while current.next and current.next.loai_tu <= new_nghia.loai_tu:
            current = current.next
        
        new_nghia.next = current.next
        current.next = new_nghia   
                
    def xem_muc_tu(self):
        temp = self.head
        while temp:
            print(temp)
            temp = temp.next
            
    
class BSTNode:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
        
    def insert (self, muc_tu):
        if not self.root:
            self.root = BSTNode(muc_tu)
        else:
            self._insert_recursive (self.root, muc_tu)
            
    def _insert_recursive(self,node, muc_tu):
        if muc_tu.muc_tu < node.info.muc_tu:
            if node.left is None:
                node.left = BSTNode(muc_tu)
            else:
                self._insert_recursive(node.left, muc_tu)
        elif muc_tu.muc_tu > node.info.muc_tu:
            if node.right is None:
                node.right = BSTNode(muc_tu)
            else:
                self._insert_recursive(node.right, muc_tu)
        else:
            # Nếu mục từ đã tồn tại, chỉ cần thêm nghĩa mới vào mục từ
            # node.muc_tu.them_muc_tu(muc_tu.meanings)
            return
    
    def find(self, muc_tu):
        return self._find_recursive(self.root, muc_tu)
    
    def _find_recursive(self, node, muc_tu):
        if not node:
            return None
        if muc_tu == node.info.muc_tu:
            # tu = MucTu('muc_tu')
            # return tu.xem_muc_tu()
            return node.info
        elif muc_tu < node.info.muc_tu:
            return self._find_recursive(node.left, muc_tu )
        else:
            return self._find_recursive(node.right, muc_tu)        

            
                

bst_dictionary = BST()
td = MucTu('muc_tu')

td.them_muc_tu('adj','map','vua')
td.them_muc_tu('adj','thap','vua')
bst_dictionary.insert(td)

print(bst_dictionary.find('muc_tu'))