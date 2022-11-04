import numpy as np

cikti = np.array([1,3,5,7,9]) # 1,3,5,7,9dan oluşan bir dizi yaratma
cikti = np.arange(1,100) # 1den 100e kadar sayılarla bir dizi
cikti = np.arange(1,100,3) # 1den 100 kadar 3er 3er bir dizi
cikti = np.zeros(10) # 10 tane 0dan oluşan bir dizi
cikti = np.ones(20) # 20 tane 1den oluşan bir dizi
cikti = np.linspace(0,100,5)  # 0dan 100e kadar 5 tane
cikti = np.linspace(0,3,9) # 0dan 3e kadar 9 tane
cikti = np.random.randint(0,10) # 0la 10 arasında rastgele bir sayı
cikti = np.random.randint(20)
cikti = np.random.randint(0,10,3) #0la 10 arasında 3 tane rastgele sayıdan dizi oluşturdu
cikti = np.random.rand(5) # 0la1 arasında satgelece 5 tane sayı
cikti = np.random.randn(5) 
cikti = np.arange(50)
cikti = cikti.reshape(5,10)

#print(cikti.sum(axis=0)) # sütunları topluyor ve bir dizi olarak veriyor
#print(cikti.sum(axis=1)) # satırları topluyor ve bir dizi olarak veriyor.

cikti = np.random.randint(1,100,10)
# print(cikti.max()) # arrayin en yüksek sayısını döndürür
# print(cikti.min()) # arrayin en küçük sayısını döndürür
# print(cikti.mean()) # arrayin ortalamasını döndürür
print(cikti.argmax()) # arraydeki en büyük değerin indexini verir.


print(cikti)