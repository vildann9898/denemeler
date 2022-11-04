import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import math

class Gercekmatik(QMainWindow):
    def __init__(self):
        super().__init__()
        self.islem = ""
        self.baslat()
        self.btn0.clicked.connect(self.b0)
        self.btn1.clicked.connect(self.b1)
        self.btn2.clicked.connect(self.b2)
        self.btn3.clicked.connect(self.b3)
        self.btn4.clicked.connect(self.b4)
        self.btn5.clicked.connect(self.b5)
        self.btn6.clicked.connect(self.b6)
        self.btn7.clicked.connect(self.b7)
        self.btn8.clicked.connect(self.b8)
        self.btn9.clicked.connect(self.b9)
        self.btnAc.clicked.connect(self.bAc)
        self.btnKapa.clicked.connect(self.bKapa)
        self.btnTopla.clicked.connect(self.bTopla)
        self.btnCikar.clicked.connect(self.bCikar)
        self.btnCarp.clicked.connect(self.bCarp)
        self.btnBol.clicked.connect(self.bBol)
        self.btnBackspace.clicked.connect(self.bBackspace)
        self.btnC.clicked.connect(self.bC)
        self.btnEsit.clicked.connect(self.bEsit)
        self.bKok.clicked.connect(self.bKarekok)

    
    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\10.10.2022 Pazartesi\Gercekmatik.ui",self)
        self.show()

    def b0(self):
        self.islem += "0"
        self.txtSonuc.setText(self.islem)

    def b1(self):
        self.islem += "1"
        self.txtSonuc.setText(self.islem)
    
    def b2(self):
        self.islem += "2"
        self.txtSonuc.setText(self.islem)
    
    def b3(self):
        self.islem += "3"
        self.txtSonuc.setText(self.islem)
    
    def b4(self):
        self.islem += "4"
        self.txtSonuc.setText(self.islem)

    def b5(self):
        self.islem += "5"
        self.txtSonuc.setText(self.islem)

    def b6(self):
        self.islem += "6"
        self.txtSonuc.setText(self.islem)

    def b7(self):
        self.islem += "7"
        self.txtSonuc.setText(self.islem)

    def b8(self):
        self.islem += "8"
        self.txtSonuc.setText(self.islem)

    def b9(self):
        self.islem += "9"
        self.txtSonuc.setText(self.islem)
    
    def bAc(self):
        self.islem += "("
        self.txtSonuc.setText(self.islem)

    def bKapa(self):
        self.islem += ")"
        self.txtSonuc.setText(self.islem)

    def bTopla(self):
        self.islem += "+"
        self.txtSonuc.setText(self.islem)

    def bCikar(self):
        self.islem += "-"
        self.txtSonuc.setText(self.islem)
    
    def bCarp(self):
        self.islem += "*"
        self.txtSonuc.setText(self.islem)

    def bBol(self):
        self.islem += "/"
        self.txtSonuc.setText(self.islem)

    def bBackspace(self):
        self.islem = self.islem[:-1]
        self.txtSonuc.setText(self.islem)
    
    def bC(self):
        self.islem = ""
        self.txtSonuc.clear()

    def bEsit(self):
        self.islem = str(eval(self.islem))
        self.txtSonuc.setText(self.islem)

    def bKarekok(self):
        self.islem = eval(self.islem)
        self.islem = str(math.sqrt(self.islem))
        self.txtSonuc.setText(self.islem)


    
    

    


uygulama = QApplication(sys.argv)
hesap_makinesi = Gercekmatik()
sys.exit(uygulama.exec_())