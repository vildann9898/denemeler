class Ucus():
    def __init__(self, kod, kalkis, varis, sure, koltuk_sayisi, yolcu_sayisi):
        self.kod = kod
        self.kalkis = kalkis
        self.varis = varis
        self.sure = sure
        self.koltuk_sayisi = koltuk_sayisi
        self.yolcu_sayisi = yolcu_sayisi
    

    def bos_göster(self):
        return self.koltuk_sayisi - self.yolcu_sayisi

    def bilet_satis(self, satis_miktar):
        bos = self.koltuk_sayisi - self.yolcu_sayisi
        if satis_miktar <= bos:
            self.yolcu_sayisi += satis_miktar
            print(f"{satis_miktar} adet bilet satılmıştır.")
        else:
            print(f"{satis_miktar} adet boş yerimiz bulunmamaktadır.")

    def bilet_iptal(self, iptal_miktar):
        if iptal_miktar <= self.yolcu_sayisi:
            self.yolcu_sayisi -= iptal_miktar
            print(f"{iptal_miktar} adet bilet iptal edilmiştir.")
        else:
            print(f"O kadar yolcu yok.")


ucus1 = Ucus("THY123","ANK","IST",70,200,30)
ucus2 = Ucus("THY414","IST","ANK",80,250,40)
print("uçuş1 boş:",ucus1.bos_göster())
print("uçuş2 boş:",ucus2.bos_göster())
ucus2.bilet_iptal(42)
print("uçuş2 boş:",ucus2.bos_göster())





