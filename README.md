[README_Bilet_Satis_Uygulamasi.md](https://github.com/user-attachments/files/22180162/README_Bilet_Satis_Uygulamasi.md)
Sinema Bilet Satış Uygulaması


Bu proje, PyQt5 ile yazılmış basit bir sinema bilet satış arayüzüdür. Kullanıcıların koltuk seçmesine, isim bilgisi girmesine ve bilet satın almasına olanak tanır. Satış bilgileri `data.json` dosyasında saklanır.

---

Özellikler
- Dinamik bilet formu: seçilen koltuk sayısına göre form alanları oluşturur.
- Tam/Öğrenci bileti seçeneği (öğrenci indirimi uygulanır).
- Satış onayı için onay kutuları ve hata uyarıları.
- Satış sonrası `data.json` dosyasını günceller ve uygulama içi bellek yapısını (`filmListesi`) de günceller.



 Gereksinimler
- Python 3.8 veya üzeri
- PyQt5



1. Sanal ortamı oluşturun ve aktifleştirin
2. Gerekli bağımlılığı yükleyin: `pip install PyQt5`.
3. Proje dosyalarını aynı dizine yerleştirin (özellikle `data.json`).
4. Uygulamayı çalıştıran ana dosyanız varsa onu çalıştırın. Bu proje parçası `BiletSatisEkrani` sınıfını içerir; ana pencere veya film seçim ekranı ile entegrasyon gerektirir. Örnek kullanım:

python
main.py içinde (örnek)
from PyQt5.QtWidgets import QApplication
from biletSatisEkrani import BiletSatisEkrani
from data import filmListesi   






