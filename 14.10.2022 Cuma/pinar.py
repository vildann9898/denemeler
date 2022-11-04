import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

class Anapencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslat()
        self.btnEiffel.clicked.connect(self.eiffel_foto_ac)
        self.btnArc.clicked.connect(self.arc_foto_ac)
        self.btnPisa.clicked.connect(self.pisa_foto_ac)
        self.btnEiffelBilgi.clicked.connect(self.eiffel_bilgi_ac)
        self.btnArcBilgi.clicked.connect(self.arc_bilgi_ac)
        self.btnPisaBilgi.clicked.connect(self.pisa_bilgi_ac)

    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\14.10.2022 Cuma\pinar.ui",self)
        self.show()
    
    def eiffel_foto_ac(self):
        self.eiffel_foto_ornek = Acilirpencere()
        self.eiffel_foto_ornek.eiffel_yap()
        

    def arc_foto_ac(self):
        self.arc_foto_ornek = Acilirpencere()
        self.arc_foto_ornek.arc_yap()
    
    def pisa_foto_ac(self):
        self.pisa_foto_ornek = Acilirpencere()
        self.pisa_foto_ornek.pisa_yap()
    
    def eiffel_bilgi_ac(self):
        self.eiffel_bilgi_ornek = Acilirpencere()
        self.eiffel_bilgi_ornek.eiffel_bilgi()

    def arc_bilgi_ac(self):
        self.arc_bilgi_ornek = Acilirpencere()
        self.arc_bilgi_ornek.arc_bilgi()

    def pisa_bilgi_ac(self):
        self.pisa_bilgi_ornek = Acilirpencere()
        self.pisa_bilgi_ornek.pisa_bilgi()

class Acilirpencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslat()

    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\14.10.2022 Cuma\acilir.ui",self)
        self.show()

    def eiffel_yap(self):
        self.fotom.setPixmap(QPixmap(r"D:\KeremHoca\denemeler\14.10.2022 Cuma\eiffel.jpg"))

    def arc_yap(self):
        self.fotom.setPixmap(QPixmap(r"D:\KeremHoca\denemeler\14.10.2022 Cuma\arc.jpg"))

    def pisa_yap(self):
        self.fotom.setPixmap(QPixmap(r"D:\KeremHoca\denemeler\14.10.2022 Cuma\pisa.jpg"))

    def eiffel_bilgi(self):
        self.fotom.setText("Fransa'da, Paris")

    def arc_bilgi(self):
        self.fotom.setText("Fransa'da, Paris")

    def pisa_bilgi(self):
        self.fotom.setText("İtalya'da, Pisa")



uygulama = QApplication(sys.argv)
anapencere1 = Anapencere()
sys.exit(uygulama.exec_())