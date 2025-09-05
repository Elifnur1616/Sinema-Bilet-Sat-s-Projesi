import json

class Koltuk:
    def __init__(self,koltukNo,koltukDurumu,alanKisi,tutar):
        self.koltukNo=koltukNo
        self.KoltukDurumu=koltukDurumu
        self.alanKisi=alanKisi
        self.Tutar=tutar

class Film:
    def __init__(self,isim,resimYolu,id,koltukBilgileri):
       self.isim=isim
       self.resimYolu=resimYolu
       self.id=id
       self.koltukBilgileri=koltukBilgileri



def veriyiAl()  :
  dosya=open("data.json")
  veri=json.load(dosya)
  filmListesi=[]
  for filmİsmi in veri.keys():
     film=veri[filmİsmi]
     koltukBilgileri=[Koltuk(koltuk['koltukNo'],koltuk['koltukDurumu'],koltuk['alanKisi'],koltuk['tutar'])for koltuk in film['koltukBilgileri']]
     filmListesi.append(Film(filmİsmi,film['image'],film['id'],koltukBilgileri))



  return filmListesi

filmListesi=veriyiAl()
print(filmListesi)