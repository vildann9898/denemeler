class Arac():
    def __init__(self, fiyat, yakit, renk):
        self.fiyat = fiyat
        self.yakit = yakit
        self.renk = renk

    def yakit_fulle(self):
        self.yakit = 100

    def yakit_bosalt(self):
        self.yakit = 0

    def kalan_yakit(self):
        return self.yakit
    
class Araba(Arac):
    def __init__(self, fiyat, yakit, renk, hiz):
        super().__init__(fiyat, yakit, renk)
        self.hiz = hiz
    
    def korna(self):
        print("Bip bip!")

class Kamyon(Arac):
    def __init__(self, fiyat, yakit, renk, tekerlek):
        super().__init__(fiyat,yakit,renk)
        self.tekerlek = tekerlek
    
    def korna(self):
        print("Darari darari!")

taksi = Araba(300000, 50, "Sarı", 180)
taksi.korna()
karahan = Kamyon(600000, 100, "Siyah", 16)
karahan.korna()
print(karahan.yakit)
karahan.yakit_bosalt()
print(karahan.yakit)
