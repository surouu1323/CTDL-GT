def count_words(file_path,find_word):
    with open(file_path, 'r') as rf: # Mở tệp và đọc từng dòng
        sentences = rf.readlines() 
    counts = dict()

    for sen in sentences: # lấy từng dòng trong file
        words = sen.lower().split() # Chuyển dòng thành chữ thường và tách thành các từ

        for word in words:  #lấy từng từ 1 trong dòng ra
            if word in counts: # kiểm tra coi từ đó đã có trong dict chưa
                counts[word] += 1 #nếu có thì +1
            else:
                counts[word] = 1    #nếu không thì tạo 1 từ mới với số lượng là 1

    return counts[find_word]

file_path = "E:/thanhdzai/stuff/dsktop/P1_data.txt"
print(count_words(file_path,"man"))
