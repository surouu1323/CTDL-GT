class Meaning:
    def __init__(self, part_of_speech, definition, example):
        self.part_of_speech = part_of_speech
        self.definition = definition
        self.example = example

    def __repr__(self):
        return f"{self.part_of_speech}: {self.definition} ({self.example})"

class Entry:
    def __init__(self, word):
        self.word = word
        self.meanings = []

    def add_meaning(self, part_of_speech, definition, example):
        meaning = Meaning(part_of_speech, definition, example)
        self.meanings.append(meaning)

    def __repr__(self):
        meanings_str = "\n".join([str(m) for m in self.meanings])
        return f"{self.word}:\n{meanings_str}"
class BSTNode:
    def __init__(self, entry):
        self.entry = entry
        self.left = None
        self.right = None

class BSTDictionary:
    def __init__(self):
        self.root = None

    def insert(self, entry):
        if not self.root:
            self.root = BSTNode(entry)
        else:
            self._insert_recursive(self.root, entry)

    def _insert_recursive(self, node, entry):
        if entry.word < node.entry.word:
            if node.left is None:
                node.left = BSTNode(entry)
            else:
                self._insert_recursive(node.left, entry)
        elif entry.word > node.entry.word:
            if node.right is None:
                node.right = BSTNode(entry)
            else:
                self._insert_recursive(node.right, entry)
        else:
            # Nếu mục từ đã tồn tại, chỉ cần thêm nghĩa mới vào mục từ
            node.entry.meanings.extend(entry.meanings)

    def delete(self, word):
        self.root = self._delete_recursive(self.root, word)

    def _delete_recursive(self, node, word):
        if not node:
            return None

        if word < node.entry.word:
            node.left = self._delete_recursive(node.left, word)
        elif word > node.entry.word:
            node.right = self._delete_recursive(node.right, word)
        else:
            # Nếu nút cần xóa được tìm thấy
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # Trường hợp có hai con, tìm nút nhỏ nhất bên phải
            min_larger_node = self._find_min(node.right)
            node.entry = min_larger_node.entry
            node.right = self._delete_recursive(node.right, min_larger_node.entry.word)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find(self, word):
        return self._find_recursive(self.root, word)

    def _find_recursive(self, node, word):
        if not node:
            return None
        if word == node.entry.word:
            return node.entry
        elif word < node.entry.word:
            return self._find_recursive(node.left, word)
        else:
            return self._find_recursive(node.right, word)

    def inorder_traversal(self):
        # Duyệt cây theo thứ tự inorder
        results = []
        self._inorder_recursive(self.root, results)
        return results

    def _inorder_recursive(self, node, results):
        if node:
            self._inorder_recursive(node.left, results)
            results.append(node.entry)
            self._inorder_recursive(node.right, results)
import json

def save_dictionary(bst, filename):
    entries = bst.inorder_traversal()
    dictionary_data = []
    for entry in entries:
        entry_data = {
            "word": entry.word,
            "meanings": [{"part_of_speech": m.part_of_speech, "definition": m.definition, "example": m.example} for m in entry.meanings]
        }
        dictionary_data.append(entry_data)

    with open(filename, 'w') as f:
        json.dump(dictionary_data, f, indent=4)

def load_dictionary(filename):
    bst = BSTDictionary()
    with open(filename, 'r') as f:
        dictionary_data = json.load(f)
        for entry_data in dictionary_data:
            entry = Entry(entry_data["word"])
            for meaning_data in entry_data["meanings"]:
                entry.add_meaning(meaning_data["part_of_speech"], meaning_data["definition"], meaning_data["example"])
            bst.insert(entry)
    return bst
def main():
    bst_dictionary = BSTDictionary()

    while True:
        print("\nDictionary Menu:")
        print("1. Add a new entry")
        print("2. Remove an entry")
        print("3. Lookup a word")
        print("4. Save dictionary")
        print("5. Load dictionary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            word = input("Enter the word: ")
            part_of_speech = input("Enter the part of speech: ")
            definition = input("Enter the definition: ")
            example = input("Enter an example: ")
            entry = Entry(word)
            entry.add_meaning(part_of_speech, definition, example)
            bst_dictionary.insert(entry)
            print("Entry added.")

        elif choice == "2":
            word = input("Enter the word to remove: ")
            bst_dictionary.delete(word)
            print("Entry removed.")

        elif choice == "3":
            word = input("Enter the word to lookup: ")
            entry = bst_dictionary.find(word)
            if entry:
                print("Meaning of", word)
                print(entry)
            else:
                print("Word not found.")

        elif choice == "4":
            filename = input("Enter the filename to save to: ")
            save_dictionary(bst_dictionary, filename)
            print("Dictionary saved.")

        elif choice == "5":
            filename = input("Enter the filename to load from: ")
            bst_dictionary = load_dictionary(filename)
            print("Dictionary loaded.")

        elif choice == "6":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
