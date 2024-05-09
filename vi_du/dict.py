class PhuongThuc:
    def __init__(self):
        # Bảng băm có 26 ô cho các ký tự từ 'a' đến 'z'
        self.table = {chr(i):{} for i in range(ord('a'), ord('z')+1)}
        
    def __hash_func(self, word):
        # Hàm băm lấy ký tự đầu tiên
        return word[0].lower() # Đảm bảo xử lý chữ hoa chữ thường
    
    def NhapTu(self, tu, tu_dong_nghia = None, tu_trai_nghia = None):
        # Tạo một từ điển cho từ này
        word_info = {
            'tu' : tu,
            'dong_nghia' : tu_dong_nghia,
            'trai_nghia' : tu_trai_nghia
        }
        # Tính vị trí trong bảng băm
        hash_key = self.__hash_func(tu)
        # Thêm từ  vào bucket
        self.table[hash_key] = word_info
        
    def TraTu(self, tu):
        # Tìm từ trong bảng băm
        hash_key = self.__hash_func(tu)
        bucket = self.table[hash_key]
        
        # Nếu từ trong danh sách bucket
        if bucket.get("tu",0) == tu:
            kq_list = ['từ:',tu,(", có từ đồng nghĩa là: ", bucket['dong_nghia']) if bucket['dong_nghia'] else '',( ", có từ trái nghĩa là: ", bucket['trai_nghia']) if bucket['trai_nghia'] else '']            
            for m in kq_list:
                print (f'{m}', end= ' ')
            print()
        else:
            print ("Không có từ cần tìm kiếm")  # Nếu không tìm thấy từ

# Tạo từ điển
tu_dien = PhuongThuc()

# Nhập các từ với từ đồng nghĩa và trái nghĩa
tu_dien.NhapTu("cao", tu_dong_nghia="lớn", tu_trai_nghia="thấp")
tu_dien.NhapTu("siêng năng", tu_dong_nghia="chăm chỉ", tu_trai_nghia="lười biếng")

# Tra từ điển
tu_dien.TraTu("cao")
tu_dien.TraTu("siêng năng")

        