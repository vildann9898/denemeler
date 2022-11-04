# iki parametre alan bir fonksiyon oluştur.
# parametrelerden biri yaş veya doğum yılı olacak.
# diğeri de isim
#emeklilik yaşı 65

def isretired(a,b):
    if a > 1000:
        if 2022-a >= 65:
            print(f"{b} emeklisiniz.")
        else:
            print(f"{b} emekliliğinize {65-(2022-a)} yıl var.")
    else:
        if a >= 65:
            print(f"{b} emeklisiniz.")
        else:
            print(f"{b} emekliliğinize {65-a} yıl var.")

yil_yas = int(input("Doğum yılınızı ve ya yaşınızı giriniz: "))
isim = input("İsminizi giriniz: ")
isretired(yil_yas,isim)

