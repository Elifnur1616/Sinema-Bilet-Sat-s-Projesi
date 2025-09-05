from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from koltukGoruntulemeEkrani import KoltukGoruntulemeEKrani
from data import filmListesi

class FilmListesiGoruntulemeEkrani(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sinema Bilet")
        self.setFixedSize(1600,800)
        self.filmListesiOlustur()
      

    def filmListesiOlustur(self):
        grid=QGridLayout()
        for index, film in enumerate(filmListesi):
            resimYolu=film.resimYolu
            
            buton=QPushButton()
            buton.setIcon(QIcon(f"filmafisleri/{resimYolu}"))
            buton.setIconSize(QSize(300,300))
            buton.setFixedSize(QSize(300,300))
            buton.setStyleSheet("background-color:black;")
            buton.clicked.connect(self.filmTiklandiCagrisi(film))


            row,col=divmod(index,3)
            grid.addWidget(buton,row,col)
        self.setLayout(grid)    

    def filmTiklandiCagrisi(self,film):
     def filmTiklandi():
       self.koltukGoruntulemeEkrani=KoltukGoruntulemeEKrani(film=film)
       self.koltukGoruntulemeEkrani.show()

     return filmTiklandi       