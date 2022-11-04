# DOSYALARIN METOT VE NİTELİKLERİ

f = open("ornek.txt","w")
# 1. closed niteliği
f.closed # dosyanın kapalı olup olmadığını kontrol eder
        # dosya kapalı ise "True" açık ise "False" cevabını döndürür
# 2. readable() metodu
f.readable() # bu metod dosyanoın okuma yetkisine
        #sahip olup olmadığını kontrol eder.
# 3. writeable() metodu
f.writable() # bu metot dosyanın yazma yetkisine
        #sahip olup olmadığını kontrol eder
# 4. truncate() metodu
f.truncate() # Herhangi bir parametre verilmediğinde
        #dosya içeriğini tamamen siler
f.truncate(10) # Dosyanın ilk 10 byte'ı dışında bütün
        #veriyi siler

f.truncate(1024*3) # 1024 byte = 1k (Dosyanın boyutunu sınırlandırıyor.)

# 5. mode niteliği
f.mode # Dosyanın hangi kipte açıldığına dair bilgi veriyor

# 6. name niteliği
f.name # dosyanın adını verir.

# 7. encoding niteliği
f.encoding # Dosyanın hangi dil kodlaması ile kodlandığını söyler ("utf-8", "cp1254")

# 8. enumerate() metodu
# Bu metod yinelenebilir bir sayaç ekler
market = ["süt","yumurta","yoğurt"]
enumerate_market = enumerate(market)
print(list(enumerate_market))