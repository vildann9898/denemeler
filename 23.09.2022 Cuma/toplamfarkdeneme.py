import toplamfark as tf
sayi1 = int(input("Bir sayı giriniz: "))
sayi2 = int(input("Bir sayı giriniz: "))
print(f"{sayi1} ile {sayi2}'nin toplamı: {tf.topfark(sayi1,sayi2)[0]} farkları: {tf.topfark(sayi1,sayi2)[1]}")