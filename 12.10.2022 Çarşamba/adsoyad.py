import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

class Adsoyadkontrol(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslat()
        self.btnKontrol.clicked.connect(self.kontrol_et)

    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\12.10.2022 Çarşamba\adsoyad.ui",self)
        self.show()

    def kontrol_et(self):
        isimsoyisimlistesi = ["Musa BOSTANCI", "Mehmet Samed ALUÇ","Çağlar TORTOPOĞLU","Vildan TOSUN","Ayşe AYTEKİN"]
        isimsoyisim = self.comboAd.currentText() + " " + self.comboSoyad.currentText()
        print(isimsoyisim)
        if isimsoyisim in isimsoyisimlistesi:
            self.label.setText("DOĞRU!")
        else:
            self.label.setText("YANLIŞ!")

uygulama = QApplication(sys.argv)
kontrolornek = Adsoyadkontrol()
sys.exit(uygulama.exec_())

sozluk = {"kerem":"yeles","musa":"bostancı"}
isim = self.comboAd.curene
soyisim = sozluk[isim]
self.label.setText(soyisim)