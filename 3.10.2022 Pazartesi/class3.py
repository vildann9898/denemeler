class Kopek():
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
    
    def konus(self):
        print(f"Merhaba benim adım {self.isim}. {self.yas} yaşındayım.")

    def ses_cikar(self):
        print("Hav hav!")

class Kedi(Kopek): # kopek classından kalıtım alsın
    def __init__(self, isim, yas, renk):
        super().__init__(isim,yas) # parent classsından kalıtım aldığını belirten kod
        self.renk = renk
    
    def ses_cikar(self): # overloading methods, overriding
        print("Miyav")

minnos = Kedi("Minnoş",3,"Turuncu")
cakir = Kopek("Süleyman",10)
cakir.ses_cikar()
minnos.ses_cikar()