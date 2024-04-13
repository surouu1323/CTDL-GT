class Dathuc:
    def __init__(self):
        self.Head = None

    def ThemSoHang(self, heso, somu):
        node = Node(heso, somu)
        if self.Head is None:
            self.Head = node
        else:
            current = self.Head
            while current.KeTiep is not None:
                current = current.KeTiep
            current.KeTiep = node

    def Tich(self, dathuc2):
        result = Dathuc()
        current1 = self.Head
        while current1 is not None:
            current2 = dathuc2.Head
            while current2 is not None:
                heso = current1.HeSo * current2.HeSo
                somu = current1.SoMu + current2.SoMu
                result.ThemSoHang(heso, somu)
                current2 = current2.KeTiep
            current1 = current1.KeTiep

        result.RutGon()
        return result

    def RutGon(self):
        current = self.Head
        while current is not None:
            next_node = current.KeTiep
            prev_node = current
            while next_node is not None:
                if current.SoMu == next_node.SoMu:
                    current.HeSo += next_node.HeSo
                    prev_node.KeTiep = next_node.KeTiep
                prev_node = next_node
                next_node = next_node.KeTiep
            current = current.KeTiep

    def inDathuc(self):
        current = self.Head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end=" ")
            current = current.KeTiep
        print()


class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None


# Tạo đa thức 1
dathuc1 = Dathuc()
dathuc1.ThemSoHang(2, 3)
dathuc1.ThemSoHang(-1, 2)
dathuc1.ThemSoHang(3, 1)
dathuc1.ThemSoHang(4, 0)
dathuc1.inDathuc()

# Tạo đa thức 2
dathuc2 = Dathuc()
dathuc2.ThemSoHang(1, 2)
dathuc2.ThemSoHang(-2, 1)
dathuc2.ThemSoHang(1, 0)
dathuc2.inDathuc()

# Tính tích của đa thức 1 và đa thức 2
tich_dathuc = dathuc1.Tich(dathuc2)

# In đa thức kết quả
tich_dathuc.inDathuc()