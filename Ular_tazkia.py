from Animal import Animal 

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_ular, warna_ular):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_ular = jenis_ular
        self.warna_ular = warna_ular

    def  info_ular(self):
        super().info_animal
        print("jenis ular \t\t : " , self.jenis_ular,
              "\nwarna ular \t\t : ", self.warna_ular)
    
ular_cobra = Ular("cobra", "memangsa ular yang tidak berbisa", "darat", "bertelur", "berbisa", "hitam dan sedikit emas")
ular_cobra.info_animal()
ular_cobra.info_ular()
print("=======================================")
ular_anakonda = Ular("anakonda", "babi hutan", "rawa", "bertelur", "tidak bebisa", "hijau")
ular_anakonda.info_animal()
ular_anakonda.info_ular()