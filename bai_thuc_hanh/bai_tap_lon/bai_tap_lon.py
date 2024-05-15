class Nghia:
    def __init__(self, loai_tu, nghia, vi_du):
        self.loai_tu = loai_tu
        self.nghia = nghia
        self.vi_du = vi_du
        self.next = None
   
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
        elif new_nghia.loai_tu == self.head.loai_tu :    
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
        nghia= []
        while current:  
            nghia.append(f"({current.loai_tu}): {current.nghia}. Ví dụ: {current.vi_du}")
            current = current.next
            
        nghia_str = '\n'.join(str(i) for i in nghia)
        return f"{self.muc_tu} \n{nghia_str}"

class BSTNode:
    def __init__(self, muc_tu):
        self.info = muc_tu
        self.left = None
        self.right = None
    
class BST:
    def __init__(self,ky_tu_dau):
        self.root = None
        self.ky_tu_dau = ky_tu_dau
        
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
        self.table = {chr(i):[] for i in range(ord('a'), ord('z')+1)}
        
    def __hash_func(self, word):
        # Hàm băm lấy ký tự đầu tiên
        return word[0].lower() # Đảm bảo xử lý chữ hoa chữ thường  
    
    def NhapTu(self, muc_tu, loai_tu, nghia, vi_du):        
        # Tính vị trí trong bảng băm
        ky_tu_dau = self.__hash_func(muc_tu)
        
        if self.table[ky_tu_dau] == []:
            td = MucTu(muc_tu)
            td.them_muc_tu(loai_tu, nghia, vi_du)
            cay_bst = BST(ky_tu_dau)
            cay_bst.insert(td)
            self.table[ky_tu_dau] = cay_bst
        elif self.table[ky_tu_dau].find(muc_tu):
            temp = self.table[ky_tu_dau].find(muc_tu)
            temp.them_muc_tu(loai_tu, nghia, vi_du)
        else:
            td = MucTu(muc_tu)
            td.them_muc_tu(loai_tu, nghia, vi_du)
            cay_bst = self.table[ky_tu_dau]
            cay_bst.insert(td)
        
    def TraTu(self, muc_tu):
        # Tìm từ trong bảng băm
        ky_tu_dau = self.__hash_func(muc_tu)
        
        if self.table[ky_tu_dau] != [] and self.table[ky_tu_dau].find(muc_tu):
            return self.table[ky_tu_dau].find(muc_tu).xem_muc_tu()
        else:
            return None
        
    def XoaTu(self, muc_tu):
        ky_tu_dau = self.__hash_func(muc_tu)
        self.table[ky_tu_dau].delete(muc_tu)
        

import json

def save_dictionary(hash):
    file_name = "N21DCDT083_bam.json"  # Tên của file JSON để lưu từ điển
    hash_table = hash.table  # Lấy bảng băm từ hash.table
    dictionary_data = []  # Danh sách để lưu dữ liệu từ điển
    
    for ky_tu_dau, bst_group in hash_table.items():
        if bst_group:  # Kiểm tra nếu nhóm BST không rỗng
            muc_tu_list = bst_group.inorder_traversal()  # Duyệt cây theo thứ tự giữa và lấy danh sách các mục từ
            
            muc_tu_dict_list = []  # Danh sách để lưu các mục từ và nghĩa của nó
            for danh_sach_nghia in muc_tu_list:
                current = danh_sach_nghia.head  # Bắt đầu từ đầu danh sách các nghĩa
                nghia_list = []  # Danh sách để lưu các nghĩa của mục từ
                
                while current:  # Duyệt qua từng nghĩa trong danh sách
                    nghia_list.append({
                        "loai_tu": current.loai_tu,  # Lấy loại từ
                        "nghia": current.nghia,  # Lấy nghĩa
                        "vi_du": current.vi_du  # Lấy ví dụ
                    })
                    current = current.next  # Chuyển đến nghĩa tiếp theo
                
                muc_tu_dict = {
                    "muc_tu": danh_sach_nghia.muc_tu,  # Lấy mục từ
                    "danh_sach_nghia": nghia_list  # Gán danh sách các nghĩa vào mục từ
                }
                muc_tu_dict_list.append(muc_tu_dict)  # Thêm mục từ vào danh sách
        
            danh_sach_bang_hash_dict = {
                "ky_tu_dau": ky_tu_dau,
                "nhieu_muc_tu": muc_tu_dict_list  # Gán danh sách các mục từ vào key đầu
            }
            dictionary_data.append(danh_sach_bang_hash_dict)  # Thêm vào danh sách dữ liệu từ điển
    
    # Mở file JSON để ghi dữ liệu
    with open(file_name, 'w') as f:
        json.dump(dictionary_data, f, indent=5)  # Ghi dữ liệu từ điển vào file JSON (indent=5)

def load_dictionary(hash):
    file_name = "N21DCDT083_bam.json"  # Tên của file JSON để lưu từ điển
    with open(file_name, 'r') as f:
        dictionary_data = json.load(f)  # Đọc dữ liệu từ file JSON
        
        for data in dictionary_data:
            ky_tu_dau = data["ky_tu_dau"]  # Lấy key đầu
            nhieu_muc_tu = data["nhieu_muc_tu"]  # Lấy danh sách các mục từ
            
            for muc_tu_data in nhieu_muc_tu:
                muc_tu = muc_tu_data["muc_tu"]  # Lấy mục từ
                danh_sach_nghia = muc_tu_data["danh_sach_nghia"]  # Lấy danh sách các nghĩa
                for phan_nghia_data in danh_sach_nghia:
                    # Nhập từng nghĩa vào bảng băm
                    hash.NhapTu(muc_tu, phan_nghia_data["loai_tu"], phan_nghia_data["nghia"], phan_nghia_data["vi_du"])


def main():
    dictionary = Hash()
    
    while True:
        print("\nChức năng:")
        print("1. Thêm một mục từ mới vào từ điển.")
        print("2. Loại bỏ một mục từ của từ điển.")
        print("3. Tra cứu các nghĩa của một mục từ trong từ điển.")
        print("4. Lưu từ điển vào các tập tin.")
        print("5. Nạp từ điển từ các tập tin")
        print("6. Kết thúc chương trình.")

        choice = input("Lựa chọn: ")

        if choice == "1":
            tu_tra_cuu = input("Nhập mục từ: ")
            loai_tu = input("Nhập loại từ : ")
            nghia = input("Nhập nghĩa: ")
            vi_du = input("Nhập ví dụ: ")    
            dictionary.NhapTu(tu_tra_cuu.lower(),loai_tu.lower(), nghia.lower(), vi_du.lower())       
            print("Thêm từ thành công.")

        elif choice == "2":
            tu_tra_cuu = input("Nhập từ cần xóa: ")
            bst = dictionary.TraTu(tu_tra_cuu)
            if bst is None:
                print ("Không có từ cần tìm kiếm")  # Nếu không tìm thấy từ
            else:
                dictionary.XoaTu(tu_tra_cuu)
                print("Xóa từ thành công.")

        elif choice == "3":
            tu_tra_cuu = input("Nhập từ cần tìm kiếm: ")
            bst = dictionary.TraTu(tu_tra_cuu)
            if bst is None:
                print ("Không có từ cần tìm kiếm")  # Nếu không tìm thấy từ
            else:
                print(bst)

        elif choice == "4": 
            save_dictionary(dictionary)
            # print("Dictionary saved.")

        elif choice == "5":
            load_dictionary(dictionary)
            print("Dictionary loaded.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()