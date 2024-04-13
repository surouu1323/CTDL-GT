class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

def dathuc_Them(dathuc, heso, somu):
    new_node = Node(heso, somu)

    if dathuc is None or somu > dathuc.SoMu:
        new_node.KeTiep = dathuc
        dathuc = new_node
    else:
        current = dathuc

        while current.KeTiep is not None and current.KeTiep.SoMu >= somu:
            current = current.KeTiep

        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    return dathuc

def dathuc_RutGon(dathuc):
    if dathuc is None or dathuc.KeTiep is None:
        return dathuc

    current = dathuc

    while current is not None and current.KeTiep is not None:
        if current.SoMu == current.KeTiep.SoMu:
            current.HeSo += current.KeTiep.HeSo
            current.KeTiep = current.KeTiep.KeTiep
        elif current.HeSo == 0:
            current.KeTiep = current.KeTiep.KeTiep
        else:
            current = current.KeTiep

    return dathuc
class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None


def dathuc_RutGon(dathuc):
    if dathuc is None or dathuc.KeTiep is None:
        return dathuc

    current = dathuc

    while current is not None and current.KeTiep is not None:
        if current.SoMu == current.KeTiep.SoMu:
            current.HeSo += current.KeTiep.HeSo
            current.KeTiep = current.KeTiep.KeTiep
        elif current.HeSo == 0:
            current.KeTiep = current.KeTiep.KeTiep
        else:
            current = current.KeTiep

    return dathuc


def inDathuc(dathuc):
    current = dathuc
    while current is not None:
        print(f"{current.HeSo}x^{current.SoMu}", end=" ")
        current = current.KeTiep
    print()


# Tạo đa thức ban đầu
dathuc = None
dathuc = dathuc_Them(dathuc, 2, 3)
dathuc = dathuc_Them(dathuc, -1, 3)
dathuc = dathuc_Them(dathuc, 3, 1)
dathuc = dathuc_Them(dathuc, 4, 0)

inDathuc(dathuc)  # Kết quả: 2x^3 - 1x^3 + 3x^1 + 4x^0

# Rút gọn đa thức
dathuc = dathuc_RutGon(dathuc)

inDathuc(dathuc)  # Kết quả: 1x^3 + 3x^1 + 4x^0