class Node:
    def __init__(self,HeSo,SoMu):
        self.HeSo = HeSo
        self.SoMu = SoMu
        self.KeTiep = None #  một tham chiếu tới nút tiếp theo trong danh sách (KeTiep).
        
class PhuongThuc:
    
    def __init__(self):
        self.head = None

    def Them(self,new_HeSo,new_SoMu): # thêm một hạng tử mới vào đa thức theo thứ tự giảm dần của số mũ.
        new_node = Node(new_HeSo,new_SoMu)
        if self.head is None: # Nếu đa thức rỗng 
            self.head = new_node # nó sẽ trở thành nút đầu tiên của đa thức
            
        else: # Nếu không, nó sẽ duyệt qua các nút trong danh sách đến khi tìm được vị trí thích hợp cho nút mới dựa trên số mũ.
            last = self.head 
            while last.KeTiep: # kiểm tra node kế tiếp nếu node đó không = none
                if last.KeTiep.SoMu < new_node.SoMu:  #nếu node kế tiếp có số mũ < số mũ node cần được thêm
                    temp = last.KeTiep # lưu giá trị kế tiếp của last vào temp
                    last.KeTiep = new_node # thay đổi giá trị kế tiếp của last thành node mới
                    new_node.KeTiep = temp # thêm giá trị kế tiếp cho node mới từ temp
                    return
                last = last.KeTiep # duyệt qua từng phần tử của list
            if last.SoMu < new_node.SoMu: # cũng giống như trên nhưng dành cho node đầu tiên 
                temp = last
                self.head = new_node
                new_node.KeTiep = temp
            else:
                last.KeTiep = new_node

    def Cong(self, DaThuc2):
        result = PhuongThuc() # tạo một đối tượng mới là result để lưu trữ kết quả phép cộng.
        p1 = self.head
        p2 = DaThuc2.head
        # Hai con trỏ p1 và p2 được sử dụng để duyệt qua hai danh sách liên kết của các hạng tử của hai đa thức.
        while p1 is not None and p2 is not None:
            # Trong quá trình duyệt, nếu hạng tử tại p1 có số mũ lớn hơn số mũ tại p2, 
            # hạng tử đó sẽ được thêm vào result và p1 sẽ di chuyển đến hạng tử tiếp theo.
            if p1.SoMu > p2.SoMu: 
                result.Them(p1.HeSo, p1.SoMu)
                p1 = p1.KeTiep
            # nếu hạng tử tại p2 có số mũ lớn hơn số mũ tại p1, 
            # hạng tử đó sẽ được thêm vào result và p2 sẽ di chuyển đến hạng tử tiếp theo.
            elif p1.SoMu < p2.SoMu:
                result.Them(p2.HeSo, p2.SoMu)
                p2 = p2.KeTiep
            else: # Nếu số mũ tại p1 và p2 bằng nhau, hệ số của hai hạng tử này sẽ được cộng lại với nhau
                heso_sum = p1.HeSo + p2.HeSo
                if heso_sum != 0: # Nếu kết quả khác 0, hạng tử mới sẽ được thêm vào result.
                    result.Them(heso_sum, p1.SoMu)
                p1 = p1.KeTiep
                p2 = p2.KeTiep
                
        # Sau khi duyệt qua tất cả các hạng tử của cả hai đa thức, các hạng tử còn lại của p1 và p2 sẽ được thêm vào result.
        while p1 is not None:
            result.Them(p1.HeSo, p1.SoMu)
            p1 = p1.KeTiep

        while p2 is not None:
            result.Them(p2.HeSo, p2.SoMu)
            p2 = p2.KeTiep

        result.RutGon() # Cuối cùng dùng phương thức RutGon được gọi để rút gọn đa thức kết quả và kết quả được trả về.
        return result
    
    def RutGon(self): # thêm một hạng tử mới vào đa thức theo thứ tự giảm dần của số mũ.
        goc = self.head
        pre_goc = goc # nút pre_goc là nút goc trước đó 
        while goc:
            search = goc.KeTiep
            while search: # bắt đầu bằng cách duyệt qua từng nút trong danh sách
                if search.SoMu == goc.SoMu: # Nếu tìm thấy một nút với số mũ giống nhau
                    goc.HeSo += search.HeSo # cộng hệ số của nút đó vào hệ số của nút gốc
                    goc.KeTiep = search.KeTiep #  loại bỏ nút đó ra khỏi danh sách
                search = search.KeTiep
                
             # Sau khi duyệt qua tất cả các nút
            if goc.HeSo == 0: # kiểm tra xem hệ số của nút goc có bằng 0 không. Nếu có loại bỏ nút đó khỏi danh sách
                # Nếu goc.KeTiep is None,tức là goc là nút cuối cùng của danh sách, 
                # nó sẽ chỉnh sửa tham chiếu từ nút trước đó (pre_goc) để trỏ tới None, loại bỏ nút goc ra khỏi danh sách.
                if goc.KeTiep == self.head: 
                    pre_goc.KeTiep = None 
                    
                # Nếu goc == self.head, tức là goc là nút đầu tiên của danh sách, 
                # nó sẽ chỉnh sửa self.head để trỏ tới nút kế tiếp của goc (goc.KeTiep), và sau đó di chuyển tham chiếu pre_goc tới self.head.
                elif goc == self.head:
                    self.head = goc.KeTiep
                    pre_goc = self.head   
                
                # Trong trường hợp còn lại, 
                # nó chỉnh sửa tham chiếu của nút trước đó (pre_goc) để trỏ tới nút kế tiếp của goc (goc.KeTiep), 
                # loại bỏ nút gốc ra khỏi danh sách.
                else:
                    pre_goc.KeTiep = goc.KeTiep
                    
            # Nếu hệ số của nút gốc không phải là 0, nó sẽ di chuyển goc tới nút kế tiếp của nó (goc = goc.KeTiep) 
            # để xử lý các nút tiếp theo trong danh sách.
            goc = goc.KeTiep

    def InDaThuc(self):
        temp = self.head
        while temp:
            if temp.HeSo > 0:  # Nếu hệ số là số dương,  in dấu cộng; 
                dau = '+'
            elif temp.HeSo < 0: # nếu là số âm, in dấu trừ. 
                dau = '-'
            else:
                dau = ' ' # nếu hệ số là 0, bỏ qua in dấu

            if (temp.HeSo == -1 or temp.HeSo == 1) and temp.SoMu > 0 : # nếu hệ số là 1 hoặc -1, bỏ qua in hệ số đó
                so = ''
            else:
                so = abs(temp.HeSo)
            
            
            # ghép các chuỗi thành một đa thức hoàn chỉnh và in ra
            if temp.SoMu == 0:
                DaThuc = ['' if temp == self.head and temp.HeSo > 0 else dau , so]
            elif temp.SoMu == 1:
                DaThuc = ['' if temp == self.head and temp.HeSo > 0 else dau, '' if so is None else so,'x']
            else:
                DaThuc = ['' if temp == self.head and temp.HeSo > 0 else dau,'' if so is None else so,'x^' if temp.SoMu > 0 else '', temp.SoMu if temp.SoMu else '']
            
            DaThuc_string = ''.join([str(m) for m in DaThuc])
            print(DaThuc_string, end=' ')
            temp = temp.KeTiep
        print()


# Tạo đa thức 1
DaThuc1 = PhuongThuc()
DaThuc1.Them(2, 3)
DaThuc1.Them(-1, 2)
DaThuc1.Them(3, 1)
DaThuc1.Them(4, 0)
DaThuc1.RutGon()
print("Đa thức 1:")
DaThuc1.InDaThuc()  # Kết quả: 2x^3 - x^2 + 3x + 4

# Tạo đa thức 2
DaThuc2 = PhuongThuc()
DaThuc2.Them(1, 2)
DaThuc2.Them(-2, 1)
DaThuc2.Them(1, 0)
DaThuc2.RutGon()
print("Đa thức 2:")
DaThuc2.InDaThuc()  # Kết quả: x^2 - 2x + 1

# Cộng hai đa thức
DaThuc_ketqua = DaThuc1.Cong(DaThuc2)
print("Đa thức 1 + đa thức 2 =")
DaThuc_ketqua.InDaThuc()  # Kết quả: 2x^3 +1x +5 