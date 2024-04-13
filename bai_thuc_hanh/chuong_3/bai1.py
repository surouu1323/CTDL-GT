class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None


def dathuc_Them(dathuc, heso, somu):
    new_node = Node(heso, somu)

    # Nếu danh sách liên kết là rỗng hoặc số mũ của số hạng mới lớn hơn số mũ của số hạng đầu tiên
    if dathuc is None or somu > dathuc.SoMu:
        new_node.KeTiep = dathuc
        dathuc = new_node
    else:
        current = dathuc

        # Tìm vị trí thích hợp để chèn số hạng mới vào danh sách liên kết
        while current.KeTiep is not None and current.KeTiep.SoMu >= somu:
            current = current.KeTiep

        new_node.KeTiep = current.KeTiep
        current.KeTiep = new_node

    return dathuc
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


def inDathuc(dathuc):
    current = dathuc
    while current is not None:
        print(f"{current.HeSo}x^{current.SoMu}", end=" ")
        current = current.KeTiep
    print()


# Tạo đa thức ban đầu
dathuc = None
dathuc = dathuc_Them(dathuc, 2, 3)
dathuc = dathuc_Them(dathuc, -1, 2)
dathuc = dathuc_Them(dathuc, 3, 1)
dathuc = dathuc_Them(dathuc, 4, 0)

inDathuc(dathuc)  # Kết quả: 2x^3 - 1x^2 + 3x^1 + 4x^0

# Thêm một số hạng mới
dathuc = dathuc_Them(dathuc, 5, 2)

inDathuc(dathuc)  # Kết quả: 2x^3 - 1x^2 + 5x^2 + 3x^1 + 4x^0