from PyQt5.QtWidgets import QWidget,QPushButton,QGridLayout,QVBoxLayout,QHBoxLayout,QMenuBar,QAction,QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QIcon,QColor
from PyQt5.QtCore import QSize,Qt

from biletSatisEkrani import BiletSatisEkrani
from data import filmListesi
class KoltukGoruntulemeEKrani(QWidget):
    def __init__(self,film):
        super().__init__()
        self.film=film
        self.secilenKoltuklar=[]
      
        self.setGeometry(300,200,1600,800)
        self.setWindowTitle(film.isim)
        self.penceregoruntusuOlustur()
        self.menuOlustur()

    def penceregoruntusuOlustur(self):
        layout=QVBoxLayout()
        self.grid=QGridLayout()
        for koltuk in self.film.koltukBilgileri:
            koltukNo=koltuk.koltukNo
            koltukDurumu=koltuk.KoltukDurumu

            buton=QPushButton(f"{koltukNo}")
            buton.setFixedSize(QSize(160,80))
            buton.clicked.connect(self.biiletSecCagrisi(koltukNo))

            if koltukDurumu:
                buton.setEnabled(False)
                buton.setStyleSheet("background-color:red;color:white;")

            else:
                buton.setEnabled(True)
                buton.setStyleSheet("background-color:green;color:white;")



            row,col=divmod(koltukNo-1,5)
            self.grid.addWidget(buton,row,col)
        self.biletAlButon=QPushButton("BİLET AL")  
        self.biletAlButon.clicked.connect(self.biletAl)
        self.biletAlButon.setFixedSize(150,50)
        self.biletAlButon.setStyleSheet("background-color:gray;color:white")
        self.biletAlButon.setEnabled(False)
        layout.addLayout(self.grid)
        layout.addWidget(self.biletAlButon,alignment=Qt.AlignmentFlag.AlignCenter)              
        self.setLayout(layout)

    def biiletSecCagrisi(self,secilenkoltukNo):
        def biletSec():
           secilenKoltuk=self.grid.itemAt(secilenkoltukNo-1).widget()
           if secilenkoltukNo not in self.secilenKoltuklar:
               self.secilenKoltuklar.append(secilenkoltukNo)
               secilenKoltuk.setStyleSheet(("background-color:yellow;color:white"))
               if len(self.secilenKoltuklar)==1:
            
                self.biletAlButon.setStyleSheet("background-color:green;color:white")
                self.biletAlButon.setEnabled(True)
           else:
                      
              self.secilenKoltuklar.remove(secilenkoltukNo)
              secilenKoltuk.setStyleSheet("background-color:green;color:white")
             
              if len(self.secilenKoltuklar)==0:
                  self.biletAlButon.setStyleSheet("background-color:gray;color:white")
                  self.biletAlButon.setEnabled(False)


        return biletSec


    def biletAl(self):
       self.close() 
       self.biletSatisEkrani=BiletSatisEkrani(film=self.film,secilenKoltuklar=self.secilenKoltuklar)
       self.biletSatisEkrani.show()
    
    def menuOlustur(self):
        menu_bar=QMenuBar(self)
        detayMenu=menu_bar.addMenu("Detay")

        biletGoruntuleAction=QAction("Biletleri Görüntüle",self)
        biletGoruntuleAction.setShortcut("Ctrl+N")
        biletGoruntuleAction.triggered.connect(self.alinanBiletleriGoruntule)
        detayMenu.addAction(biletGoruntuleAction)
       
    def alinanBiletleriGoruntule(self)   :
         self.window=QWidget()
         self.window.setWindowTitle("Alinan Biletler")
         self.window.setGeometry(150,100,800,800)
         doluKoltuklar=self.doluKoltuklariBul()

       
         biletGoruntuleTable=QTableWidget(self.window)
         biletGoruntuleTable.setFixedSize(800,800)
         biletGoruntuleTable.setRowCount(len(doluKoltuklar)+1)
         biletGoruntuleTable.setColumnCount(3)
 
         koltukNoHeader=QTableWidgetItem("Koltuk No")
         koltukNoHeader.setBackground(QColor(255,0,0))
         biletGoruntuleTable.setItem(0,0,koltukNoHeader)

         
         alanKisiHeader=QTableWidgetItem("Alan Kisi")
         alanKisiHeader.setBackground(QColor(255,0,0))
         biletGoruntuleTable.setItem(0,1,alanKisiHeader)

         
         biletTutarHeader=QTableWidgetItem("Bilet Tutar")
         biletTutarHeader.setBackground(QColor(255,0,0))
         biletGoruntuleTable.setItem(0,2,biletTutarHeader)

          
         for index,koltuk in enumerate(doluKoltuklar):
             biletGoruntuleTable.setItem(index+1,0,QTableWidgetItem(str(koltuk.koltukNo)))
             biletGoruntuleTable.setItem(index+1,1,QTableWidgetItem(str(koltuk.alanKisi)))
             biletGoruntuleTable.setItem(index+1,2,QTableWidgetItem(str(koltuk.Tutar)))





         self.window.show()
    def doluKoltuklariBul(self): 
            doluKoltuklar=[]
            id=int(self.film.id)
            for koltuk in filmListesi[id-1].koltukBilgileri:
                if koltuk.KoltukDurumu==1:
                    doluKoltuklar.append(koltuk)

         
            return doluKoltuklar