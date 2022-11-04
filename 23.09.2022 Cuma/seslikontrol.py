sesliler = "aeiıuüoö"
def seslimi(a):
    sayac = 0
    for i in a:
        if i in sesliler:
            sayac += 1
    return sayac
