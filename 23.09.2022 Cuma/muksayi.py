# girilen sayının mükemmel bir sayı olup olmadığını veren bir fonskiyon

# 1 + 2 + 3 = 6
# 1 + 2 + 4 + 7 + 14 = 28

def muksayi(a):
    toplam = 0
    for i in range(1,a):
        if a%i == 0:
            toplam +=i
    return toplam == a

def muksayiuzun(a):
    liste = []
    for i in range(1,a):
        if a%i==0:
            liste.append(i)
    toplam = 0
    for i in liste:
        toplam+=i
    if toplam == a:
        return True
    return False

print(muksayiuzun(28))