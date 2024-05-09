import json

dictionary = {
    "apple": 5,
    "banana": 3,
    "orange": 7
}

file_name = "mãsinhviên_mang.json"

# Mở tệp để ghi dữ liệu
with open(file_name, 'w') as json_file:
    json.dump(dictionary, json_file, indent=4)


# Mở tệp để đọc dữ liệu
with open(file_name, 'r') as json_file:
    loaded_dictionary = json.load(json_file)

print(loaded_dictionary)  # Output: {'apple': 5, 'banana': 3, 'orange': 7}



def main():
    while True:
        print("\nDictionary Menu:")
        print("1. Add a new entry")
        print("2. Remove an entry")
        print("3. Lookup meanings")
        print("4. Save dictionary")
        print("5. Load dictionary")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            word = input("Enter the word: ")
            part_of_speech = input("Enter the part of speech: ")
            definition = input("Enter the definition: ")
            example = input("Enter an example: ")
            print("Entry added.")

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid option, please try again.")

main()
