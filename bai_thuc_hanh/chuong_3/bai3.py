class Node:
    def __init__(self,HeSo,SoMu):
        self.HeSo = HeSo
        self.SoMu = SoMu
        self.KeTiep = None
        
class PhuongThuc:
    
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        node = Node(heso, somu)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.KeTiep is not None:
                current = current.KeTiep
            current.KeTiep = node

    def Cong(self, DaThuc2):
        result = PhuongThuc()
        p1 = self.head
        p2 = DaThuc2.head

        while p1 is not None and p2 is not None:
            if p1.SoMu > p2.SoMu:
                result.Them(p1.HeSo, p1.SoMu)
                p1 = p1.KeTiep
            elif p1.SoMu < p2.SoMu:
                result.Them(p2.HeSo, p2.SoMu)
                p2 = p2.KeTiep
            else:
                heso_sum = p1.HeSo + p2.HeSo
                if heso_sum != 0:
                    result.Them(heso_sum, p1.SoMu)
                p1 = p1.KeTiep
                p2 = p2.KeTiep

        while p1 is not None:
            result.Them(p1.HeSo, p1.SoMu)
            p1 = p1.KeTiep

        while p2 is not None:
            result.Them(p2.HeSo, p2.SoMu)
            p2 = p2.KeTiep

        result.RutGon()
        return result
    
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


# Tạo đa thức 1
DaThuc1 = PhuongThuc()
DaThuc1.Them(2, 3)
DaThuc1.Them(-2, 3)
DaThuc1.Them(-1, 2)
DaThuc1.Them(3, 1)
DaThuc1.Them(4, 0)
DaThuc1.RutGon()
DaThuc1.InDaThuc()  # Kết quả: 2x^3 - 1x^2 + 3x^1 + 4x^0

# Tạo đa thức 2
DaThuc2 = PhuongThuc()
DaThuc2.Them(1, 2)
DaThuc2.Them(-2, 1)
DaThuc2.Them(1, 0)
DaThuc2.RutGon()
DaThuc2.InDaThuc()  # Kết quả: 1x^2 - 2x^1 + 1x^0

# Cộng hai đa thức
DaThuc_ketqua = DaThuc1.Cong(DaThuc2)
DaThuc_ketqua.InDaThuc()  # Kết quả: 3x^3 - 3x^1 + 5x^0