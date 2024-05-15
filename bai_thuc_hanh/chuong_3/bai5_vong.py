class Node:
    def __init__(self,HeSo,SoMu):
        self.HeSo = HeSo
        self.SoMu = SoMu
        self.KeTiep = None
        
class PhuongThuc:
    
    def __init__(self):
        self.head = None

    def Them(self,new_HeSo,new_SoMu): # thêm một hạng tử mới vào đa thức theo thứ tự giảm dần của số mũ.
        new_node = Node(new_HeSo,new_SoMu)
        if self.head is None: # Nếu đa thức rỗng 
            self.head = new_node # nó sẽ trở thành nút đầu tiên của đa thức
            new_node.next = self.head
            
        else: # Nếu không, nó sẽ duyệt qua các nút trong danh sách đến khi tìm được vị trí thích hợp cho nút mới dựa trên số mũ.
            last = self.head 
            while last.KeTiep and (last.KeTiep != self.head): # kiểm tra node kế tiếp nếu node đó không = none
                if last.KeTiep.SoMu < new_node.SoMu:  #nếu node kế tiếp có số mũ < số mũ node cần được thêm
                    temp = last.KeTiep # lưu giá trị kế tiếp của last vào temp
                    last.KeTiep = new_node # thay đổi giá trị kế tiếp của last thành node mới
                    new_node.KeTiep = temp # thêm giá trị kế tiếp cho node mới từ temp
                    return
                last = last.KeTiep # duyệt qua từng phần tử của list
                
            if last.SoMu < new_node.SoMu: # cũng giống như trên nhưng dành cho node đầu tiên 
                temp = last
                self.head = new_node
                temp.KeTiep = self.head
                new_node.KeTiep = temp
            else:
                new_node.KeTiep = self.head
                last.KeTiep = new_node
    
    def RutGon(self):
        goc = self.head
        pre_goc = goc # nút pre_goc là nút goc trước đó 
        while True:
            search = goc.KeTiep
            while search != goc: # bắt đầu bằng cách duyệt qua từng nút trong danh sách
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
                    goc_cu = goc # lưu lại giá trị gốc cũ
                    self.head = goc.KeTiep # thay đổi head của node bằng giá trị tiếp theo
                    pre_goc = self.head   # cho pre_goc về head của node
                    temp = self.head # vì ta đã bỏ đi gốc cũ nên cần phải thay đổi giá trị kế tiếp của node cuối cùng 
                    while True:
                        temp = temp.KeTiep # trỏ đến node kế tiếp
                        if temp.KeTiep == goc_cu: # nếu node kế tiếp chỉ đến giá trị của goc_cu (là gốc mà ta đã xóa)
                            break
                    temp.KeTiep == self.head # thay đổi giá trị của node kế tiếp về lại giá trị head mới 
                
                # Trong trường hợp còn lại, 
                # nó chỉnh sửa tham chiếu của nút trước đó (pre_goc) để trỏ tới nút kế tiếp của goc (goc.KeTiep), 
                # loại bỏ nút gốc ra khỏi danh sách.
                else:
                    pre_goc.KeTiep = goc.KeTiep
                    
            # Nếu hệ số của nút gốc không phải là 0, nó sẽ di chuyển goc tới nút kế tiếp của nó (goc = goc.KeTiep) 
            # để xử lý các nút tiếp theo trong danh sách.
            goc = goc.KeTiep
            if goc == self.head:
                break 
    
    def InDaThuc(self):
        temp = self.head
        while True:
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
            
            if temp == self.head:
                break
        print()
    
    def Tich(self, DaThuc2):
        result = PhuongThuc() # Tạo một đối tượng mới là result để lưu trữ kết quả phép nhân.
        current1 = self.head 
        
        while True: # Sử dụng con trỏ current1 để duyệt qua danh sách liên kết của đa thức thứ nhất.
            current2 = DaThuc2.head
            while True:
                heso = current1.HeSo * current2.HeSo
                somu = current1.SoMu + current2.SoMu
                result.Them(heso, somu)
                current2 = current2.KeTiep
                if current2 == DaThuc2.head:
                    break
            current1 = current1.KeTiep
            if current1 == self.head:
                break
            
        result.RutGon()
        return result

# Tạo đa thức 1
DaThuc1 = PhuongThuc()
DaThuc1.Them(2, 3)
DaThuc1.Them(-1, 2)
DaThuc1.Them(3, 1)
DaThuc1.Them(4, 0)
print("Đa thức 1:")
DaThuc1.InDaThuc()

# Tạo đa thức 2
DaThuc2 = PhuongThuc()
DaThuc2.Them(1, 2)
DaThuc2.Them(-2, 1)
DaThuc2.Them(1, 0)
print("Đa thức 2:")
DaThuc2.InDaThuc()

# Tính tích của đa thức 1 và đa thức 2
tich_DaThuc = DaThuc1.Tich(DaThuc2)

print("Tích của 2 đa thức")
# In đa thức kết quả
tich_DaThuc.InDaThuc()