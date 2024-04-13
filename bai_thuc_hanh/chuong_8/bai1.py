class TuDien:
    def __init__(self):
        self.tudien = {}

    def NhapTu(self, tu, dongnghia=None, trainghia=None):
        ky_tu_dau = tu[0]
        if ky_tu_dau not in self.tudien:
            self.tudien[ky_tu_dau] = []

        self.tudien[ky_tu_dau].append({
            'tu': tu,
            'dongnghia': dongnghia,
            'trainghia': trainghia
        })

    def TraTu(self, tu):
        ky_tu_dau = tu[0]
        if ky_tu_dau in self.tudien:
            for word in self.tudien[ky_tu_dau]:
                if word['tu'] == tu:
                    return word['dongnghia'], word['trainghia']

        return None, None
    
td = TuDien()

td.NhapTu('mèo', 'cat', 'chó')
td.NhapTu('chó', 'dog', 'mèo')
td.NhapTu('bàn', 'table', 'ghế')
td.NhapTu('ghế', 'chair', 'bàn')

dongnghia, trainghia = td.TraTu('mèo')
print(dongnghia, trainghia)  # Kết quả: cat, chó

dongnghia, trainghia = td.TraTu('bàn')
print(dongnghia, trainghia)  # Kết quả: table, ghế

dongnghia, trainghia = td.TraTu('abc')
print(dongnghia, trainghia)  # Kết quả: None, None