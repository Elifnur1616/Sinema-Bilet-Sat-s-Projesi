from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLineEdit,QMessageBox,QLabel
from PyQt5.QtCore import QSize,Qt
from filmListesiGoruntulemeEkrani import FilmListesiGoruntulemeEkrani

kullaniciAdi="elifnur atici"
sifre="1234"

class GirisEkrani(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bilet Satis")
        self.setFixedSize(400,150)

        vbox=QVBoxLayout()
        hboxKullaniciAdi=QHBoxLayout()
        self.kullaniciAdiLabel=QLabel("Kullanici Adi:")
        self.kullaniciAdiLineEdit=QLineEdit()
        self.kullaniciAdiLineEdit.setFixedSize(QSize(200,20))
        hboxKullaniciAdi.addWidget(self.kullaniciAdiLabel)
        hboxKullaniciAdi.addWidget(self.kullaniciAdiLineEdit)

        hboxsifre=QHBoxLayout()
        self.sifreLabel=QLabel("şifre:")
        self.sifreLineEdit=QLineEdit()
        self.sifreLineEdit.setEchoMode(QLineEdit.Password)
        self.sifreLineEdit.setFixedSize(QSize(200,20))
        hboxsifre.addWidget(self.sifreLabel)
        hboxsifre.addWidget(self.sifreLineEdit)


        self.buton=QPushButton()
        self.buton.setText("giris yap")
        self.buton.setFixedSize(100,30)
        self.buton.clicked.connect(self.girisYap)
    






        vbox.addLayout(hboxKullaniciAdi)
        vbox.addLayout(hboxsifre)
        vbox.addWidget(self.buton,alignment=Qt.AlignmentFlag.AlignCenter)
        self.setLayout(vbox)
 

    def girisYap(self):
        if self.kullaniciAdiLineEdit.text()==kullaniciAdi and self.sifreLineEdit.text()==sifre:
            self.close()
            self.filmListesiGoruntulemeEkrani=FilmListesiGoruntulemeEkrani()
            self.filmListesiGoruntulemeEkrani.show()
        else:
            QMessageBox.warning(self,"HATA","KULLANİCİ BİLGİLERİ HATALİ")    