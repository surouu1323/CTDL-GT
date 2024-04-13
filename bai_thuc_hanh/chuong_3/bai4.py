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

    def DoiDau(self):
        current = self.Head
        while current is not None:
            current.HeSo = -current.HeSo
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


# Tạo đa thức
dathuc = Dathuc()
dathuc.ThemSoHang(2, 3)
dathuc.ThemSoHang(-1, 2)
dathuc.ThemSoHang(3, 1)
dathuc.ThemSoHang(4, 0)

dathuc.inDathuc()  # Kết quả: 2x^3 - 1x^2 + 3x^1 + 4x^0

# Đổi ngược dấu đại số của mỗi số hạng trong đa thức
dathuc.DoiDau()

dathuc.inDathuc()  # Kết quả: -2x^3 + 1x^2 - 3x^1 - 4x^0