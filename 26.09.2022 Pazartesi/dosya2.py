#dosyanın ortasında değişiklik yapma
with open("rehber.txt","r+") as f:
    veri = f.readlines()
    veri.insert(2,"Murat: 5375373753\n")
    f.seek(0)
    f.writelines(veri)