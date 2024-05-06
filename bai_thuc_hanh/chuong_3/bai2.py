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
                    last.KeTiep = new_node
                    return
                last = last.KeTiep
            last.KeTiep = new_node
        
    def RutGon(self):
        goc = self.head
        pre_goc = goc
        while goc:
            search = goc.KeTiep
            while search:
                if search.SoMu == goc.SoMu:
                    goc.HeSo += search.HeSo
                    goc.KeTiep = search.KeTiep
                search = search.KeTiep
            if goc.HeSo == 0:
                if goc.KeTiep is None:
                    pre_goc.KeTiep = None
                elif goc == self.head:
                    self.head = goc.KeTiep
                    pre_goc = self.head   
                else:
                    pre_goc.KeTiep = goc.KeTiep
                goc = pre_goc
            else:
                goc = goc.KeTiep

        
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
DaThuc.Them(-2,2)
DaThuc.Them(2,2)
DaThuc.Them(-2,2)
DaThuc.Them(3,1)
DaThuc.Them(-3,1)
DaThuc.Them(-3,0)
DaThuc.InDaThuc()
print("\n")
DaThuc.RutGon()
DaThuc.InDaThuc()