import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtGui import QPixmap

class KediKopek(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslat()
        self.btnKedi.clicked.connect(self.kedi)
        self.btnKopek.clicked.connect(self.kopek)

    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\10.10.2022 Pazartesi\kedikopek.ui",self)
        self.show()
    
    def kedi(self):
        self.fotom.setPixmap(QPixmap(r"D:\KeremHoca\denemeler\10.10.2022 Pazartesi\kedi.jpg"))
    
    def kopek(self):
        self.fotom.setPixmap(QPixmap(r"D:\KeremHoca\denemeler\10.10.2022 Pazartesi\kopek.jpg"))

uygulama = QApplication(sys.argv)
kerem = KediKopek()
sys.exit(uygulama.exec_())
