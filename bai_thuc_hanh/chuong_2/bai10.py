def NhomCot(mang):
    cols = len(mang[0])
    rows = len(mang)

    groups = {}  # Dùng từ điển để lưu trữ nhóm chỉ mục cột giống nhau

    for i in range(cols):
        column = [mang[k][i] for k in range(rows)]
        column_str = str(column)  # Chuyển đổi cột thành chuỗi để lưu trữ trong từ điển

        if column_str not in groups:
            groups[column_str] = [i]
        else:
            groups[column_str].append(i)

    for group in groups.values():
        print(' '.join(map(str, group)))
