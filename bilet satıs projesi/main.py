import sys
from PyQt5.QtWidgets import QApplication
from girisEkrani import GirisEkrani
app=QApplication(sys.argv)

girisEkranı=GirisEkrani()
girisEkranı.show()
sys.exit(app.exec_())