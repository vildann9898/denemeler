class Kopek():
    def __init__(self, isim, yas): 
        self.isim = isim
        self.yas = yas

    def ses_cikar(self):
        print(f"Merhaba benim adım {self.isim}. {self.yas} yaşındayım.")

    def yas_degistir(self, yeni_yas):
        self.yas = yeni_yas
    
    def kilo_ekle(self, yeni_kilo):
        self.kilo = yeni_kilo

zeytin = Kopek("Zeytin",15)
findik = Kopek("Fındık",3)
zeytin.kilo_ekle(30)
print(zeytin.kilo)
findik.kilo_ekle(4)
print(findik.kilo)



