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

    def Tich(self, DaThuc2):
        result = PhuongThuc()
        current1 = self.head
        while current1 is not None:
            current2 = DaThuc2.head
            while current2 is not None:
                heso = current1.HeSo * current2.HeSo
                somu = current1.SoMu + current2.SoMu
                result.Them(heso, somu)
                current2 = current2.KeTiep
            current1 = current1.KeTiep

        result.RutGon()
        return result

# Tạo đa thức 1
DaThuc1 = PhuongThuc()
DaThuc1.Them(2, 3)
DaThuc1.Them(-1, 2)
DaThuc1.Them(3, 1)
DaThuc1.Them(4, 0)
DaThuc1.InDaThuc()

# Tạo đa thức 2
DaThuc2 = PhuongThuc()
DaThuc2.Them(1, 2)
DaThuc2.Them(-2, 1)
DaThuc2.Them(1, 0)
DaThuc2.InDaThuc()

# Tính tích của đa thức 1 và đa thức 2
tich_DaThuc = DaThuc1.Tich(DaThuc2)

# In đa thức kết quả
tich_DaThuc.InDaThuc()