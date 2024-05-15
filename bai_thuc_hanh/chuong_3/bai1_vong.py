class Node:
    def __init__(self,HeSo,SoMu):
        self.HeSo = HeSo # Mỗi nút chứa hai thuộc tính: HeSo (hệ số) và SoMu (số mũ),
        self.SoMu = SoMu
        self.KeTiep = None #  một tham chiếu tới nút tiếp theo trong danh sách (KeTiep).
                
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
            
DaThuc = PhuongThuc()
DaThuc.Them(3,1)

DaThuc.Them(1,2)
DaThuc.Them(4,0)

DaThuc.InDaThuc() # x^2 +3x^1 +4x 