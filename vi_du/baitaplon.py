class Nghia:
    def __init__ (self, loai_tu, nghia, vi_du):
        self.loai_tu = loai_tu
        self.nghia = nghia
        self.vi_du = vi_du
        self.ke_tiep = None
        
    def __repr__ (self):
        return f"({self.loai_tu}): {self.nghia}. Ví dụ: {self.vi_du}"
    
        
class MucTu:
    def __init__ (self,loai_tu):
        self.loai_tu = loai_tu
        self.muc_tu = []
        
    def them_muc_tu (self, loai_tu, nghia, vi_du):
        new_nghia = Nghia (loai_tu, nghia, vi_du)
        
        if 