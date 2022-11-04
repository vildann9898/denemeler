# vücut kitle indeksi hesaplama
# bmi = kilo/boy**2
boy = input("boy")
kilo = input("kilo")
def bmi(a,b):
    if isinstance(a,int):
        a /= 100 # a = a/100
    vki= b/a**2
    if