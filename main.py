from  PyQt5 import  QtWidgets
import  sys
from PyQt5.QtWidgets import QApplication
from  giris import Ui_GirisEkrani
from  anaEkran import Ui_anaEkran
from  guncelle import Ui_guncelleEkrani
from  kayitEkle import Ui_kayitEkrani
import Sifreleme
import DataAccess


secilmisKayit = []



class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedWidth(360)
        self.setFixedHeight(175)
        self.ui = Ui_GirisEkrani()
        self.ui.setupUi(self)
        self.ekran = None
        self.ui.girisButton.clicked.connect(self.girisFonksiyon)

    def girisFonksiyon(self):
        password = self.ui.passwordTextBox.text()
        result = DataAccess.IdileAra("1")
        if result !=None:
            decryptSifre = Sifreleme.decryptSifre(result[2])
            decryptSifre = str(decryptSifre,'utf8')
            if password == decryptSifre:
                if self.ekran is None:
                    self.ekran = AnaEkran()
                self.ekran.show()
                self.close()
            else:
                self.ui.label_2.setVisible(True)
        else:
            Sifreleme.generate_key()
            encryptSifre = Sifreleme.encryptSifre(self.ui.passwordTextBox.text())
            DataAccess.AnaSifreEkle(encryptSifre)
            if self.ekran is None:
                self.ekran = AnaEkran()
            self.ekran.show()
            self.close()


class AnaEkran(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(420)
        self.setFixedHeight(320)
        self.ui = Ui_anaEkran()
        self.ui.setupUi(self)
        self.ekran = None
        self.ui.yeniKayitEkleButton.clicked.connect(self.yeniKayitEkranaGec)
        self.ui.kayitGuncelleButton.clicked.connect(self.guncelleEkranaGec)
        self.ui.kayitSilButton.clicked.connect(self.KayitSil)
        self.ui.cikisButton.clicked.connect(self.Cikis)
        self.ui.sifreGosterButton.clicked.connect(self.SifreyiGoster)


    def SifreyiGoster(self):
        row = self.ui.sifreTablo.currentRow()
        secilenId = self.ui.sifreTablo.item(row, 0).text()
        data = DataAccess.IdileAra(secilenId)
        if data != None:
            sifre = str(Sifreleme.decryptSifre(data[2]), 'utf8')
            self.ui.CozulmusSifreTextBox.setText(sifre)


    def Cikis(self):
        self.close()


    def yeniKayitEkranaGec(self):
        if self.ekran is None:
            self.ekran = KayitEkleEkran()
        self.ekran.show()
        self.hide()

    def guncelleEkranaGec(self):
        row = self.ui.sifreTablo.currentRow()
        secilmisKayit.clear()
        secilmisKayit.append(self.ui.sifreTablo.item(row,0).text())
        data = DataAccess.IdileAra(secilmisKayit[0])
        if data != None:
            sifre = str(Sifreleme.decryptSifre(data[2]), 'utf8')
            secilmisKayit.append(data[1])
            secilmisKayit.append(sifre)


        if self.ekran is None:
            self.ekran = Guncelle()
            self.ekran.show()
            self.hide()
    def KayitSil(self):
        row = self.ui.sifreTablo.currentRow()
        secilmisKayit.clear()
        if row > 0:
            secilmisKayit.append(self.ui.sifreTablo.item(row,0).text())
            DataAccess.IdileKayitSilSql(secilmisKayit[0])
        else:

            secilmisKayit.append(self.ui.sifreTablo.item(0, 0).text())
            DataAccess.IdileKayitSilSql(secilmisKayit[0])


class KayitEkleEkran(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(370)
        self.setFixedHeight(305)
        self.ui = Ui_kayitEkrani()
        self.ui.setupUi(self)
        self.ekran = None
        self.ui.yeniKayitGeriButton.clicked.connect(self.geriDon)
        self.ui.yeniKayitOnaylaButton.clicked.connect(self.KayitOnayla)


    def geriDon(self):
        if self.ekran is None:
            self.ekran = AnaEkran()
        self.ekran.show()
        self.close()

    def KayitOnayla(self):
        uygulama = self.ui.yeniKayitUygulamaAdiTextBox.text()
        sifre = self.ui.yeniKayitSifreTextBox.text()
        sifre = Sifreleme.encryptSifre(sifre)
        DataAccess.KayitEkleSql(sifre,uygulama)
        if self.ekran is None:
            self.ekran = AnaEkran()
        self.ekran.show()
        self.close()




class Guncelle(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedWidth(370)
        self.setFixedHeight(305)
        self.ui = Ui_guncelleEkrani()
        self.ui.setupUi(self)
        self.ekran = None
        self.ui.guncelleIDTextBox.setText(secilmisKayit[0])
        self.ui.guncelleUygulamaTextBox.setText(secilmisKayit[1])
        self.ui.guncelleSifreTextBox.setText(secilmisKayit[2])
        self.ui.guncelleGeriButton.clicked.connect(self.geriDon)
        self.ui.guncelleOnaylaButton.clicked.connect(self.KayitGuncelle)

    def geriDon(self):
        if self.ekran is None:
            self.ekran = AnaEkran()
        self.ekran.show()
        self.close()
    def KayitGuncelle(self):
        sifreId = self.ui.guncelleIDTextBox.text()
        uygulama = self.ui.guncelleUygulamaTextBox.text()
        sifre = self.ui.guncelleSifreTextBox.text()
        sifre = Sifreleme.encryptSifre(sifre)
        DataAccess.IdileGuncelleSql(uygulama,sifre,sifreId)
        if self.ekran is None:
            self.ekran = AnaEkran()
        self.ekran.show()
        self.close()





app = QApplication(sys.argv)
ekran = Login()
ekran.show()
app.exec_()





