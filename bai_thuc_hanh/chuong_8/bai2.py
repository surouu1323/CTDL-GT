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

    def DongNghia(self, tu):
        ky_tu_dau = tu[0]
        dongnghia = []
        if ky_tu_dau in self.tudien:
            for word in self.tudien[ky_tu_dau]:
                if word['tu'] == tu and word['dongnghia'] is not None:
                    dongnghia.append(word['dongnghia'])
        return dongnghia

    def TraiNghia(self, tu):
        ky_tu_dau = tu[0]
        trainghia = []
        if ky_tu_dau in self.tudien:
            for word in self.tudien[ky_tu_dau]:
                if word['tu'] == tu and word['trainghia'] is not None:
                    trainghia.append(word['trainghia'])
        return trainghia
    
tudien = TuDien()

tudien.NhapTu("mèo", dongnghia=["mimi", "meomeo"], trainghia=["chó"])
tudien.NhapTu("chó", dongnghia=["dog"], trainghia=["mèo", "gà"])

print(tudien.DongNghia("mèo"))  # Output: ['mimi', 'meomeo']
print(tudien.DongNghia("chó"))  # Output: ['dog']
print(tudien.TraiNghia("mèo"))  # Output: ['chó']
print(tudien.TraiNghia("chó"))  # Output: ['mèo', 'gà']