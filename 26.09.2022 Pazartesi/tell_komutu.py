# bize imlecin o anda dosya içerisinde hangi byte dizininde olduğunu söyler
f = open("python.txt","r")
print(f.read()) # read imleci en sonda bırakıyor
print(f.tell()) # imlecin yerini söylüyor
f.seek(10) # imleci 10. bytea götürüyor
print(f.tell()) # imlecin yerini söylüyor