class TuDien:
    def __init__(self):
        self.tudien = {}

    def NhapAlbum(self, ten_album, bai_hat):
        self.tudien[ten_album] = bai_hat

    def XemAlbum(self, ten):
        if ten in self.tudien:
            album = self.tudien[ten]
            print("Thông tin album:", ten)
            for bai_hat in album:
                print("Tên bài hát:", bai_hat['ten_bai_hat'])
                print("Tên nhạc sĩ sáng tác:", bai_hat['ten_nhac_si'])
                print("Tên ca sĩ:", bai_hat['ten_ca_si'])
                print()
        else:
            print("Album không tồn tại trong từ điển.")
            
tudien = TuDien()

bai_hat_album1 = [
    {
        'ten_bai_hat': 'Bài hát 1',
        'ten_nhac_si': 'Nhạc sĩ 1',
        'ten_ca_si': 'Ca sĩ 1'
    },
    {
        'ten_bai_hat': 'Bài hát 2',
        'ten_nhac_si': 'Nhạc sĩ 2',
        'ten_ca_si': 'Ca sĩ 2'
    }
]

bai_hat_album2 = [
    {
        'ten_bai_hat': 'Bài hát A',
        'ten_nhac_si': 'Nhạc sĩ A',
        'ten_ca_si': 'Ca sĩ A'
    },
    {
        'ten_bai_hat': 'Bài hát B',
        'ten_nhac_si': 'Nhạc sĩ B',
        'ten_ca_si': 'Ca sĩ B'
    }
]

tudien.NhapAlbum("Album 1", bai_hat_album1)
tudien.NhapAlbum("Album 2", bai_hat_album2)

tudien.XemAlbum("Album 1")
tudien.XemAlbum("Album 2")
tudien.XemAlbum("Album 3")