import numpy as np

sayilar = np.array([1,2,3,4,5,6,7,8,9])

cikti = sayilar[5]
cikti = sayilar[-1]
cikti = sayilar[0:3]
cikti = sayilar[:3]
cikti = sayilar[3:]
cikti = sayilar[::]
cikti = sayilar[::-1]

sayilar2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
cikti = sayilar2[0]
cikti = sayilar2[0,2] # 0. indexin 2. indexini veriyor
cikti = sayilar2[:,2] # hepsinin 2. indexini veriyor
cikti = sayilar2[:,0] # hepsinin 0. indexini veriyor
cikti = sayilar2[:,0:2] # hepsinin 0dan 2. indexine kadar veriyor
cikti = sayilar2[-1,:] # -1. indexin hepsini veriyor
cikti = sayilar2[-1,::-1] # üsttekinin tersi
cikti = sayilar2[:2,:2] # 2. indexe kadar olanların içindekilerinin 2. indexine kadar olanlarını veriyor

print(cikti)
