
class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None  #  một tham chiếu tới nút tiếp theo trong danh sách (KeTiep).

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
            while search and search != self.head: # bắt đầu bằng cách duyệt qua từng nút trong danh sách
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
    
    def DoiDau(self):
        current = self.head
        while True:
            current.HeSo = -current.HeSo
            current = current.KeTiep
            if current == self.head:
                break
        
# Tạo đa thức
DaThuc = PhuongThuc()
DaThuc.Them(2, 3)
DaThuc.Them(-1, 2)
DaThuc.Them(3, 1)
DaThuc.Them(4, 0)
print("Đa thức :")
DaThuc.InDaThuc()  # Kết quả: 2x^3 - 1x^2 + 3x^1 + 4x^0

# Đổi ngược dấu đại số của mỗi số hạng trong đa thức
DaThuc.DoiDau()
print("Đa thức đổi dấu:")
DaThuc.InDaThuc()  # Kết quả: -2x^3 + 1x^2 - 3x^1 - 4x^0