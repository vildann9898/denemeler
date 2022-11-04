sayilar= []
while True :
  sayı = input("sayı giriniz= ")
  if sayı == "e":
    print("çıkış yapıldı.")
    break
  elif sayı.isdigit():   
    sayı = int(sayı)    
    sayilar.append(sayı)  
  else:   
    print("sayı giriniz.")   
  
def listem1(a):
  tek_sayilar = []
  cift_sayilar = []
  for i in a:
    if i%2==0:
      cift_sayilar.append(i)
    else:
      tek_sayilar.append(i)
  return tek_sayilar, cift_sayilar
  
print(f"tek sayılar liste: {listem1(sayilar)[0]}")
print(f"çift sayılar liste: {listem1(sayilar)[1]}")

