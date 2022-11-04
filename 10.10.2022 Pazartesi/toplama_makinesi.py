import sys #Platform bağımsız olduğu için hangi sistemde çalışıyorsan onun çalışma prensiplerini alması için
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic # User interface controller. (input-output kontrolü)


class toplama_makinesi(QMainWindow): # main windowdan kalıtım aldık (penceremdeki elementlere ulaşabileyim)
    def __init__(self):
        super().__init__() # kalıtım yapmak için
        self.baslat()
        self.btnSonuc.clicked.connect(self.hesapla)


    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\10.10.2022 Pazartesi\toplama_makinesi.ui", self)
        self.show()

    def hesapla(self):
        self.sayi1 = self.txtSayi1.text()
        self.sayi2 = self.txtSayi2.text()
        sonuc = int(self.sayi1) + int(self.sayi2)
        self.txtSonuc.setText(str(sonuc))

uygulama = QApplication(sys.argv)
tm = toplama_makinesi()
sys.exit(uygulama.exec_())