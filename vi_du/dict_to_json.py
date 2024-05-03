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
