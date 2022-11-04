liste = ["a","b","c"]
for i in liste:
    print(f"{liste.index(i)}:{i}")
print("**************************")
for i,y in enumerate(liste):
    print(f"{i}:{y}")