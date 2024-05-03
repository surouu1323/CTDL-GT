class Meaning:
    def __init__(self, part_of_speech, definition, example):
        self.loai_tu = part_of_speech
        self.dinh_nghia = definition
        self.vd = example

    def __repr__(self):
        return f"{self.loai_tu}: {self.dinh_nghia} ({self.vd})"

class them_phan:
    def __init__(self,tu):
        self.tu = tu
        self.nhieu_nghia = []
    def them_nghia(self,loai_tu, dinh_nghia, vd):
        nghia = Meaning(loai_tu,dinh_nghia,vd)
        self.nhieu_nghia.append(nghia)
    def __repr__(self):
        nghia_str = "\n".join(str(m) for m in self.nhieu_nghia)
        return f"{self.tu}:\n{nghia_str}"
    
    
class BSTNode:
    def __init__(self,tu_moi):
        self.tu_moi = tu_moi
        self.left = None
        self.right = None   

class BSTDictionary:
    def __init__(self):
        self.root = None
        
    def insert(self,tu_moi):
        if not self.root:
            self.root = BSTNode(tu_moi)
        else:
            self._insert(self.root, tu_moi)      
                
    def _insert(self,node,tu_moi):
        if tu_moi.tu < node.tu_moi.tu:
            if node.left is None:
                node.left = BSTNode(tu_moi)
            else:
                self.insert(node.left,tu_moi)
        elif tu_moi.tu > node.tu_moi.tu:
            if node.right is None:
                node.right = BSTNode(tu_moi)
            else:
                self.insert(node.right,tu_moi)    
        else:
            # Nếu mục từ đã tồn tại, chỉ cần thêm nghĩa mới vào mục từ
            node.tu_moi.nhieu_nghia.extend(tu_moi.nhieu_nghia)
    
    def find(self, word):
        return self._find(self.root, word)
    
    def _find(self,node, tu):
        if not self.root:
            return None
        else:
            if tu == node.tu_moi.tu:
                return node.tu_moi
            elif tu < node.tu_moi.tu:
                return self.find_recursive(node.left, tu)
            else:
                return self.find_recursive(node.right, tu)
            
    def inorder_traversal(self):
        # Duyệt cây theo thứ tự inorder
        ket_qua = []
        self._inorder_recursive(self.root, ket_qua)
        return ket_qua

    def _inorder_recursive(self, node, ket_qua):
        if node:
            self._inorder_recursive(node.left, ket_qua)
            ket_qua.append(node.tu_moi)
            self._inorder_recursive(node.right, ket_qua)
 
import json

def save_dictionary(bst, filename):
    entries = bst.inorder_traversal()
    dictionary_data = []
    for entry in entries:
        entry_data = {
            "word": entry.tu,
            "meanings": [{"part_of_speech": m.loai_tu, "definition": m.dinh_nghia, "example": m.vd} for m in entry.nhieu_nghia]
        }
        dictionary_data.append(entry_data)

    with open(filename, 'w') as f:
        json.dump(dictionary_data, f, indent=4)

def load_dictionary(filename):
    bst = BSTDictionary()
    with open(filename, 'r') as f:
        dictionary_data = json.load(f)
        for entry_data in dictionary_data:
            entry = them_phan(entry_data["word"])
            for meaning_data in entry_data["meanings"]:
                entry.them_nghia(meaning_data["part_of_speech"], meaning_data["definition"], meaning_data["example"])
            bst.insert(entry)
    return bst
   
    
def main():
    Tu_dien = BSTDictionary()

    while True:
        print("\nDictionary Menu:")
        print("1. Thêm từ mới")
        print("2. Xóa từ cũ")
        print("3. Tìm kiếm")
        print("4. Xuất file")
        print("5. Thêm file")
        print("6. Thoát")

        lua_chon = input("Nhập lựa chọn: ")

        if lua_chon == "1":
            tu = input("Nhập từ cần thêm: ")
            loai_tu = input("Loại từ: ")
            nghia = input("Nghĩa: ")
            vd = input("Ví dụ: ")
            them_tu_moi = them_phan(tu)
            them_tu_moi.them_nghia(loai_tu, nghia, vd)
            Tu_dien.insert(them_tu_moi)
            print("Thêm từ mới thành công.")

        elif lua_chon == "2":
            word = input("Nhập từ cần xóa: ")
            Tu_dien.delete(word)
            print("Xóa từ thành công.")

        elif lua_chon == "3":
            word = input("Nhập từ cần tìm kiếm: ")
            entry = Tu_dien.find(word)
            if entry:
                print("Nghĩa của từ", word)
                print(entry)
            else:
                print("Từ không có trong từ điển.")

        elif lua_chon == "4":
            save_dictionary(Tu_dien, "N21DCDT083_BST")
            print("Xuất từ điển thành công.")

        elif lua_chon == "5":
            Tu_dien = load_dictionary("N21DCDT083_BST")
            print("Thêm từ điểm thành công.")

        elif lua_chon == "6":
            print("Thoát chương trình.")
            break

        else:
            print("Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
