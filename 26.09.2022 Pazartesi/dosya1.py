#dosyanın başında değişiklik yapma
with open("rehber.txt","r+") as f: # rehber.txt dosyasını f olarak açıyor
    veri = f.read() # dosyadakileri veri değişkenine kaydediyor
    f.seek(0) #imleci en başa getiriyor
    f.write("Mustafa: 5065065060\n" + veri) # istediklerimizi yazdırıyor
