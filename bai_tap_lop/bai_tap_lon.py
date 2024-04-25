class Node:
    def __init__(self, word, meanings):
        self.word = word
        self.meanings = meanings
        self.left = None
        self.right = None

class DictionaryBST:
    def __init__(self):
        self.root = None

    def insert(self, word, meanings):
        if not self.root:
            self.root = Node(word, meanings)
        else:
            self._insert_recursive(self.root, word, meanings)

    def _insert_recursive(self, node, word, meanings):
        if word < node.word:
            if node.left is None:
                node.left = Node(word, meanings)
            else:
                self._insert_recursive(node.left, word, meanings)
        elif word > node.word:
            if node.right is None:
                node.right = Node(word, meanings)
            else:
                self._insert_recursive(node.right, word, meanings)
        else:  # Trường hợp từ đã tồn tại, thêm nghĩa mới
            node.meanings.extend(meanings)

    def remove(self, word):
        self.root = self._remove_recursive(self.root, word)

    def _remove_recursive(self, node, word):
        if node is None:
            return node
        if word < node.word:
            node.left = self._remove_recursive(node.left, word)
        elif word > node.word:
            node.right = self._remove_recursive(node.right, word)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.word = successor.word
                node.meanings = successor.meanings
                node.right = self._remove_recursive(node.right, successor.word)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, word):
        return self._search_recursive(self.root, word)

    def _search_recursive(self, node, word):
        if node is None or node.word == word:
            return node
        if word < node.word:
            return self._search_recursive(node.left, word)
        return self._search_recursive(node.right, word)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            self._save_to_file_recursive(self.root, f)

    def _save_to_file_recursive(self, node, f):
        if node:
            f.write(f"{node.word}: {', '.join(node.meanings)}\n")
            self._save_to_file_recursive(node.left, f)
            self._save_to_file_recursive(node.right, f)

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                word, meanings = line.strip().split(': ')
                meanings_list = meanings.split(', ')
                self.insert(word, meanings_list)

def display_menu():
    print("----- Menu -----")
    print("1. Thêm từ mới")
    print("2. Xóa từ")
    print("3. Tra từ điển")
    print("4. Lưu từ điển vào tập tin")
    print("5. Nạp từ điển từ tập tin")
    print("6. Kết thúc")

def main():
    dictionary = DictionaryBST()

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-6): ")

        if choice == '1':
            word = input("Nhập từ mới: ")
            meanings = input("Nhập nghĩa của từ, phân tách bởi dấu phẩy: ").split(',')
            dictionary.insert(word.strip(), [meaning.strip() for meaning in meanings])
            print("Từ mới đã được thêm vào từ điển.")
        elif choice == '2':
            word = input("Nhập từ cần xóa: ")
            if dictionary.remove(word.strip()):
                print("Từ đã được xóa khỏi từ điển.")
            else:
                print("Từ không tồn tại trong từ điển.")
        elif choice == '3':
            word = input("Nhập từ cần tra: ")
            node = dictionary.search(word.strip())
            if node:
                print(f"{node.word}: {', '.join(node.meanings)}")
            else:
                print("Từ không tồn tại trong từ điển.")
        elif choice == '4':
            filename = input("Nhập tên tập tin để lưu từ điển: ")
            dictionary.save_to_file(filename.strip())
            print("Từ điển đã được lưu vào tập tin.")
        elif choice == '5':
            filename = input("Nhập tên tập tin để nạp từ điển: ")
            dictionary.load_from_file(filename.strip())
            print("Từ điển đã được nạp từ tập tin.")
        elif choice == '6':
            print("Kết thúc chương trình.")
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn lại.")

if __name__ == "_main_":
    main() 