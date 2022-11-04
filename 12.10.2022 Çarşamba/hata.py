import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic

class Hatadeneme(QMainWindow):
    def __init__(self):
        super().__init__()
        self.baslat()
        self.btnHata.clicked.connect(self.bHata)

    def baslat(self):
        uic.loadUi(r"D:\KeremHoca\denemeler\12.10.2022 Çarşamba\hata.ui",self)
        self.show()
    
    def bHata(self):
        msg = QMessageBox()
        msg.setWindowTitle("WindowTitle") # popup (açılır pencere)'in başlığı
        msg.setText("setText") #popupdaki ana yazıyı değiştiriyor
        msg.setInformativeText("informativeText")
        msg.setIcon(QMessageBox.Question) #icon ve ses ayarlıyor.
        msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore) # buton ekleme
        msg.setDefaultButton(QMessageBox.Ignore) # varsayılan butonu Ognore yaptık.
        msg.setDetailedText("detay detay detay detay detay detay detay detay detay ") # hatayla ilgili daha fazla bilgi vermek için açılır kapanır bir buton
        msg.buttonClicked.connect(self.pop_up_button) #butona tıklandığında bu methoda git

        x = msg.exec_() # popup'ı gösteren kod.
    
    def pop_up_button(self, i): # i = buton
        print(i.text()) # butonun textini yazdır




uygulama = QApplication(sys.argv)
hataornek = Hatadeneme()
sys.exit(uygulama.exec_())
