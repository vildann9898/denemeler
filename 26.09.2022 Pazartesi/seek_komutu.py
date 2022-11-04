# seek komutu imleci parametrede belirttiğimiz byte pozisyonuna getiriyor.
f = open("python.txt","r")
print(f.read())
f.seek(0) # "0" parametresi ile imleç dosyanın en başındaki byte konumuna gelir.