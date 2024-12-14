from Animal import Animal 

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_air, warna_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.warna_ikan = warna_ikan

    def  info_ikan(self):
        super().info_animal
        print("Jenis air \t\t : ", self.jenis_air,
              "\nWarna ikan \t\t : ", self.warna_ikan)
        
    
ikan_hiu = Ikan("hiu", "plankton", "air", "bertelur", "air laut", "abu abu")
ikan_hiu.info_animal()
ikan_hiu.info_ikan()
print("=======================================")
ikan_lele = Ikan("lele", "pelet", "air", "bertelur", "tawar", "hitam")
ikan_lele.info_animal()
ikan_lele.info_ikan()






