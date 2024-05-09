class Node:
    def __init__(self,HeSo,SoMu):
        self.HeSo = HeSo
        self.SoMu = SoMu
        self.KeTiep = None
        
class PhuongThuc:
    def __init__(self):
        self.head = None
    
    def Them(self,new_HeSo,new_SoMu):
        new_node = Node(new_HeSo,new_SoMu)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.KeTiep:
                if last.KeTiep.SoMu < new_node.SoMu:
                    temp = last.KeTiep
                    last.KeTiep = new_node
                    new_node.KeTiep = temp
                    return
                last = last.KeTiep
            if last.SoMu < new_node.SoMu:
                temp = last
                self.head = new_node
                new_node.KeTiep = temp
            else:
                last.KeTiep = new_node
        
    def InDaThuc(self):
        temp = self.head
        while temp:
            
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
            
            
            DaThuc = [dau if temp != self.head or temp.HeSo < 0 else '','' if so is None else so,'x','^' if temp.SoMu else '', temp.SoMu if temp.SoMu else '']
            DaThuc_string = ''.join([str(m) for m in DaThuc])
            print(DaThuc_string, end=' ')
            temp = temp.KeTiep
        print()
            
DaThuc = PhuongThuc()
DaThuc.Them(3,1)

DaThuc.Them(1,2)
DaThuc.Them(4,0)

DaThuc.InDaThuc()