class Kopek():
    def __init__(self, isim): # Kopek class'ından bir nesne oluşturduğumuz içindeki kodlar çalışıyor.
        self.isim = isim

    def ses_cikar(self):
        print(f"Merhaba benim adım {self.isim}.")

zeytin = Kopek("Zeytin") # Kopek class'ından bir nesne oluşturduk
findik = Kopek("Fındık")
print(zeytin.isim)
print(findik.isim)
findik.ses_cikar()
zeytin.ses_cikar()

