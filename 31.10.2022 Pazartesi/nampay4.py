import numpy as np

dizi1 = np.random.randint(10,100,6)
dizi2 = np.random.randint(10,100,6)

# print(dizi1)
# print(dizi2)

cikti = dizi1 + dizi2
cikti = dizi1 + 10
cikti = dizi1 * dizi2
cikti = dizi1 / dizi2

cikti = np.sin(dizi1)
cikti = np.sqrt(dizi2)
cikti = np.log(dizi2)
cikti = np.cos(dizi2)

cokludizi1 = dizi1.reshape(2,3)
cokludizi2 = dizi2.reshape(2,3)

# print(cokludizi1)
# print(cokludizi2)

cikti = np.vstack((cokludizi1, cokludizi2)) # (vertical stack = dikey birleştir)
cikti = np.hstack((cokludizi1, cokludizi2)) # (horizontal stack = yatay birleştir)

cikti = dizi1 >= 50
cikti = dizi1 % 2 == 0

print(dizi1)
print(dizi1[cikti])
print(cikti)
