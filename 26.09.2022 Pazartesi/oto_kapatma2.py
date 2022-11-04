#dosyaları otomatik kapatma

try:
    dosya = open("deneme.txt","r")
  #  .... dosya ile ilgili işlemler
   # ... hata veren bir kod
except IOError:
    print("bir hata oluştu")
finally:
    dosya.close()