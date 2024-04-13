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

    def Chep(self):
        copy_dathuc = Dathuc()
        current = self.Head
        while current is not None:
            copy_dathuc.ThemSoHang(current.HeSo, current.SoMu)
            current = current.KeTiep
        return copy_dathuc

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


# Tạo đa thức gốc
dathuc = Dathuc()
dathuc.ThemSoHang(2, 3)
dathuc.ThemSoHang(-1, 2)
dathuc.ThemSoHang(3, 1)
dathuc.ThemSoHang(4, 0)

# Sao chép đa thức
copy_dathuc = dathuc.Chep()

# In đa thức gốc
print("Đa thức gốc:")
dathuc.inDathuc()

# In đa thức sao chép
print("Đa thức sao chép:")
copy_dathuc.inDathuc()