import numpy as np

# python list (python listesi)
listem = [1,2,3,4,5,6,7,8,9]

# numpy array (numpy dizisi)
arrayim = np.array([1,2,3,4,5,6,7,8,9])

# print(type(listem))
# print(type(arrayim)) # nd = n dimensional = n boyut

# print(listem)
# print(arrayim)

coklu_listem = [[1,2,3],[4,5,6],[7,8,9]]
coklu_arrayim = arrayim.reshape(3, 3) # 3 e 3 matris olarak şekillendirir

# print(coklu_listem)
# print(coklu_arrayim)

# print(arrayim.ndim) # arrayin kaç boyuttan oluştuğunu söylüyor
# print(coklu_arrayim.ndim)

print(arrayim.shape) # arrayin şeklini söylüyor
print(coklu_arrayim.shape)
