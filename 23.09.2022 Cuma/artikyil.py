# 4'e tam bölünen ama 100'e tam bölünmeyen yıllar artık yıl
# 400'e tam bölünen yıllar da artık yıl
def isleap_year(x):
    if x % 4 == 0 and x % 100 != 0:
        return True
    elif x % 400 == 0:
        return True
    else:
        return False

while True:
    year = input("Enter a year: ")
    if year == "q":
        print("Loop ended")
        break
    else:
        print(isleap_year(int(year)))