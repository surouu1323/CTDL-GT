class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
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
    
    def DoiDau(self):
        current = self.head
        while current is not None:
            current.HeSo = -current.HeSo
            current = current.KeTiep

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

# Tạo đa thức
DaThuc = PhuongThuc()
DaThuc.Them(2, 3)
DaThuc.Them(-1, 2)
DaThuc.Them(3, 1)
DaThuc.Them(4, 0)

DaThuc.InDaThuc()  # Kết quả: 2x^3 - 1x^2 + 3x^1 + 4x^0

# Đổi ngược dấu đại số của mỗi số hạng trong đa thức
DaThuc.DoiDau()

DaThuc.InDaThuc()  # Kết quả: -2x^3 + 1x^2 - 3x^1 - 4x^0