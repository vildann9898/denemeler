# kullanıcının girdiği parolada türkçe karakter var ise False
# yok ise True veren bir fonksiyon yazın
parola = input("parola giriniz: ") # şifre
def trkontrol(a):
    tr_cr = "ığüşÇöIĞÜÖÇ"
    for i in a:
        if i in tr_cr:
            return False
        else:
            continue
    return True

print(trkontrol(parola))
    

