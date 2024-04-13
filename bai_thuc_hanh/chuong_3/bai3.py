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

    def Cong(self, dathuc2):
        result = Dathuc()
        p1 = self.Head
        p2 = dathuc2.Head

        while p1 is not None and p2 is not None:
            if p1.SoMu > p2.SoMu:
                result.ThemSoHang(p1.HeSo, p1.SoMu)
                p1 = p1.KeTiep
            elif p1.SoMu < p2.SoMu:
                result.ThemSoHang(p2.HeSo, p2.SoMu)
                p2 = p2.KeTiep
            else:
                heso_sum = p1.HeSo + p2.HeSo
                if heso_sum != 0:
                    result.ThemSoHang(heso_sum, p1.SoMu)
                p1 = p1.KeTiep
                p2 = p2.KeTiep

        while p1 is not None:
            result.ThemSoHang(p1.HeSo, p1.SoMu)
            p1 = p1.KeTiep

        while p2 is not None:
            result.ThemSoHang(p2.HeSo, p2.SoMu)
            p2 = p2.KeTiep

        result.RutGon()
        return result

    def RutGon(self):
        if self.Head is None:
            return

        current = self.Head
        while current is not None and current.KeTiep is not None:
            if current.SoMu == current.KeTiep.SoMu:
                current.HeSo += current.KeTiep.HeSo
                current.KeTiep = current.KeTiep.KeTiep
            elif current.HeSo == 0:
                current.KeTiep = current.KeTiep.KeTiep
            else:
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

dathuc1.inDathuc()  # Kết quả: 2x^3 - 1x^2 + 3x^1 + 4x^0

# Tạo đa thức 2
dathuc2 = Dathuc()
dathuc2.ThemSoHang(1, 2)
dathuc2.ThemSoHang(-2, 1)
dathuc2.ThemSoHang(1, 0)

dathuc2.inDathuc()  # Kết quả: 1x^2 - 2x^1 + 1x^0

# Cộng hai đa thức
dathuc_ketqua = dathuc1.Cong(dathuc2)
dathuc_ketqua.inDathuc()  # Kết quả: 3x^3 - 3x^1 + 5x^0