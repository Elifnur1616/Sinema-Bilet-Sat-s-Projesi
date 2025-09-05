from PyQt5.QtWidgets import QWidget,QPushButton,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QRadioButton,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from data import filmListesi
import json



class BiletSatisEkrani(QWidget):
    def __init__(self,film,secilenKoltuklar):
        super().__init__()
        self.film=film
        self.secilenKoltuklar=secilenKoltuklar
        self.lineEditListesi=[]

        self.secilenKoltukSayisi=len(secilenKoltuklar)

        self.toplamTutar=20.0*self.secilenKoltukSayisi

        dinamikFormUzunlugu=self.secilenKoltukSayisi*180
       
        self.setFixedSize(400,dinamikFormUzunlugu)

        self.setWindowTitle(film.isim)
        self.formOlustur() 


    def formOlustur(self):
        layout=QVBoxLayout()
        for koltukNo in self.secilenKoltuklar:
            koltukNoLabel= QLabel()
            koltukNoLabel.setText(f"Koltuk No:{koltukNo}")

            layout.addWidget(koltukNoLabel)
            hBoxKullaniciBilgisi=QHBoxLayout()
            isimSoysimLabel=QLabel("isim soyisim:")

            isimSoysimLineEdit=QLineEdit()
            self.lineEditListesi.append(isimSoysimLineEdit)
            hBoxKullaniciBilgisi.addWidget(isimSoysimLabel)
            hBoxKullaniciBilgisi.addWidget(isimSoysimLineEdit)
            layout.addLayout(hBoxKullaniciBilgisi)




 
        hboxBiletBigisi=QHBoxLayout()
        tamBiletRadioButon=QRadioButton("TAM BİLET")

        tamBiletRadioButon.setChecked(True)
        tamBiletRadioButon.toggled.connect(self.biletTuruSecildi)
        ogrenciBiletRadioButon=QRadioButton("ÖGRENCİ BİLET")
        ogrenciBiletRadioButon.toggled.connect(self.biletTuruSecildi)

        hboxBiletBigisi.addWidget(tamBiletRadioButon)    
        hboxBiletBigisi.addWidget(ogrenciBiletRadioButon)
        layout.addLayout(hboxBiletBigisi)

        self.toplamTutarLabel=QLabel()
        self.toplamTutarLabel.setText(f"Toplam Tutar:{self.toplamTutar}")
        layout.addWidget(self.toplamTutarLabel)

        self.biletAlButon=QPushButton("BİLET AL")
        self.biletAlButon.clicked.connect(self.biletAlTiklandi)
        layout.addWidget(self.biletAlButon)




        self.setLayout(layout)

    def biletTuruSecildi(self):
        radio_button=self.sender()
        if radio_button.isChecked() and radio_button.text()=="ÖGRENCİ BİLET":
            self.toplamTutar-=5.0*self.secilenKoltukSayisi

        elif radio_button.isChecked() and radio_button.text()=="TAM BİLET":
            self.toplamTutar+=5.0*self.secilenKoltukSayisi
        self.toplamTutarLabel.setText(f"TOPLAM TUTAR:{self.toplamTutar}")

    def biletAlTiklandi(self):
        for lineEdit in self.lineEditListesi:
            if len(lineEdit.text())==0:
                QMessageBox.warning(self,"HATA!","Eksik bilgiler mevcut.")
                return
            
        kullaniciCevabi=QMessageBox.question(self,"Bilet Satis",f"Toplam tutar:{self.toplamTutar}. Bilet satisini onayliyor musunuz?",QMessageBox.Yes |QMessageBox.No )
        if kullaniciCevabi==QMessageBox.Yes:    
           self.biletAl()          

    def biletAl(self)  :
        dosya=open("data.json","r")
        veri=json.load(dosya)
        dosya.close()


        for index,lineEdit in enumerate(self.lineEditListesi):  
            secilenKoltukNo=int(self.secilenKoltuklar[index])
                                                   
            veri[f"{self.film.isim}"]["koltukBilgileri"][(secilenKoltukNo-1)]["koltukDurumu"]=1    
            veri[f"{self.film.isim}"]["koltukBilgileri"][secilenKoltukNo-1]["alanKisi"]=lineEdit.text()
            veri[f"{self.film.isim}"]["koltukBilgileri"][secilenKoltukNo-1]["tutar"]=self.toplamTutar/self.secilenKoltukSayisi  

            id=int(self.film.id)

            filmListesi[id-1].koltukBilgileri[secilenKoltukNo-1].koltukDurumu=1
            filmListesi[id-1].koltukBilgileri[secilenKoltukNo-1].alanKisi=lineEdit.text()
            filmListesi[id-1].koltukBilgileri[secilenKoltukNo-1].tutar=self.toplamTutar/self.secilenKoltukSayisi
             
        dosya=open("data.json","w")  
        dosya.write(json.dumps(veri,indent=4))   
        dosya.close()                         
        
        QMessageBox.information(self,"BARARİLİ","Bilet Basariyla Alindi")
        self.close()