import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

class Pencere1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslat()
        self.btnMusa.clicked.connect(self.musa_ac)
        self.btnKerem.clicked.connect(self.kerem_ac)

    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\14.10.2022 Cuma\pencere1.ui",self)
        self.show()

    def musa_ac(self):
        self.pencere2 = Pencere2()
    def kerem_ac(self):
        self.pencere3 = Pencere3()

class Pencere2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslat()
        self.btnKerem.clicked.connect(self.kerem_ac)

    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\14.10.2022 Cuma\pencere2.ui",self)
        self.show()

    def kerem_ac(self):
        self.pencere3 = Pencere3()

class Pencere3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslat()
        self.btnMusa.clicked.connect(self.musa_ac)

    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\14.10.2022 Cuma\pencere3.ui",self)
        self.show()

    def musa_ac(self):
        self.pencere2 = Pencere2() 

uygulama = QApplication(sys.argv)
ornek = Pencere1()
sys.exit(uygulama.exec_())
