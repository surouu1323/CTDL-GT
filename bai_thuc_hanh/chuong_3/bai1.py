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
        
    def InDaThuc(self):
        temp = self.head
        while temp:
            # Nếu hệ số là số dương,  in dấu cộng; 
            # nếu là số âm, in dấu trừ. 
            # nếu hệ số là 1 hoặc -1, bỏ qua in hệ số đó
            if temp.HeSo > 0:
                dau = '+'
            elif temp.HeSo < 0:
                dau = '-'
            else:
                dau = '-'
            if temp.HeSo == 1 or temp.HeSo == -1:
                so = None
            else:
                so = abs(temp.HeSo)
            
            # ghép các chuỗi thành một đa thức hoàn chỉnh và in ra
            DaThuc = [dau if temp != self.head or temp.HeSo < 0 else '','' if so is None else so,'x','^' if temp.SoMu else '', temp.SoMu if temp.SoMu else '']
            DaThuc_string = ''.join([str(m) for m in DaThuc])
            print(DaThuc_string, end=' ')
            temp = temp.KeTiep
        print()
            
DaThuc = PhuongThuc()
DaThuc.Them(3,1)

DaThuc.Them(1,2)
DaThuc.Them(4,0)

DaThuc.InDaThuc() # x^2 +3x^1 +4x 