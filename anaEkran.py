from PyQt5 import QtCore, QtGui, QtWidgets
import  DataAccess


class Ui_anaEkran(object):

    def loadData(self):
        result = DataAccess.KayitlariAlSql()
        self.sifreTablo.setRowCount(0)
        if(len(result)>0):
            for i in range(len(result)):
                self.sifreTablo.insertRow(i)
                self.sifreTablo.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
                self.sifreTablo.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
                self.sifreTablo.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))


    def Ara(self):
        text = self.lineEdit.text()
        result = DataAccess.UygulamaileAra(text)
        self.sifreTablo.setRowCount(0)
        if (len(result) > 0):
            for i in range(len(result)):
                self.sifreTablo.insertRow(i)
                self.sifreTablo.setItem(i, 0, QtWidgets.QTableWidgetItem(str(result[i][0])))
                self.sifreTablo.setItem(i, 1, QtWidgets.QTableWidgetItem(str(result[i][1])))
                self.sifreTablo.setItem(i, 2, QtWidgets.QTableWidgetItem(str(result[i][2])))


    def setupUi(self, anaEkran):
        anaEkran.setObjectName("anaEkran")
        anaEkran.resize(420, 320)
        anaEkran.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.sifreTablo = QtWidgets.QTableWidget(anaEkran)
        self.sifreTablo.setGeometry(QtCore.QRect(10, 110, 235, 192))
        self.sifreTablo.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.sifreTablo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sifreTablo.setProperty("showDropIndicator", False)
        self.sifreTablo.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.sifreTablo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sifreTablo.setRowCount(0)
        self.sifreTablo.setColumnCount(3)
        self.sifreTablo.setObjectName("sifreTablo")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        item.setFont(font)
        self.sifreTablo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        item.setFont(font)
        self.sifreTablo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        item.setFont(font)
        self.sifreTablo.setHorizontalHeaderItem(2, item)
        self.sifreTablo.horizontalHeader().setDefaultSectionSize(77)
        self.sifreTablo.horizontalHeader().setMinimumSectionSize(47)
        self.yeniKayitEkleButton = QtWidgets.QPushButton(anaEkran)
        self.yeniKayitEkleButton.setGeometry(QtCore.QRect(20, 20, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yeniKayitEkleButton.sizePolicy().hasHeightForWidth())
        self.yeniKayitEkleButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.yeniKayitEkleButton.setFont(font)
        self.yeniKayitEkleButton.setAutoFillBackground(False)
        self.yeniKayitEkleButton.setStyleSheet("")
        self.yeniKayitEkleButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/ekle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.yeniKayitEkleButton.setIcon(icon)
        self.yeniKayitEkleButton.setIconSize(QtCore.QSize(32, 32))
        self.yeniKayitEkleButton.setFlat(True)
        self.yeniKayitEkleButton.setObjectName("yeniKayitEkleButton")
        self.kayitSilButton = QtWidgets.QPushButton(anaEkran)
        self.kayitSilButton.setGeometry(QtCore.QRect(70, 20, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kayitSilButton.sizePolicy().hasHeightForWidth())
        self.kayitSilButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.kayitSilButton.setFont(font)
        self.kayitSilButton.setAutoFillBackground(False)
        self.kayitSilButton.setStyleSheet("")
        self.kayitSilButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/sil.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kayitSilButton.setIcon(icon1)
        self.kayitSilButton.setIconSize(QtCore.QSize(32, 32))
        self.kayitSilButton.setFlat(True)
        self.kayitSilButton.setObjectName("kayitSilButton")
        self.listeYenileButton = QtWidgets.QPushButton(anaEkran)
        self.listeYenileButton.setGeometry(QtCore.QRect(190, 20, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listeYenileButton.sizePolicy().hasHeightForWidth())
        self.listeYenileButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.listeYenileButton.setFont(font)
        self.listeYenileButton.setAutoFillBackground(False)
        self.listeYenileButton.setStyleSheet("")
        self.listeYenileButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/yenile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.listeYenileButton.setIcon(icon2)
        self.listeYenileButton.setIconSize(QtCore.QSize(32, 32))
        self.listeYenileButton.setFlat(True)
        self.listeYenileButton.setObjectName("listeYenileButton")
        self.listeYenileButton.clicked.connect(self.loadData)
        self.cikisButton = QtWidgets.QPushButton(anaEkran)
        self.cikisButton.setGeometry(QtCore.QRect(320, 280, 75, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cikisButton.sizePolicy().hasHeightForWidth())
        self.cikisButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.cikisButton.setFont(font)
        self.cikisButton.setStyleSheet("background-color: rgb(0, 184, 0);\n"
"alternate-background-color: rgb(0, 225, 0);")
        self.cikisButton.setObjectName("cikisButton")
        self.kayitGuncelleButton = QtWidgets.QPushButton(anaEkran)
        self.kayitGuncelleButton.setGeometry(QtCore.QRect(130, 20, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kayitGuncelleButton.sizePolicy().hasHeightForWidth())
        self.kayitGuncelleButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.kayitGuncelleButton.setFont(font)
        self.kayitGuncelleButton.setAutoFillBackground(False)
        self.kayitGuncelleButton.setStyleSheet("")
        self.kayitGuncelleButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/guncelle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kayitGuncelleButton.setIcon(icon3)
        self.kayitGuncelleButton.setIconSize(QtCore.QSize(32, 32))
        self.kayitGuncelleButton.setFlat(True)
        self.kayitGuncelleButton.setObjectName("kayitGuncelleButton")
        self.sifreGosterButton = QtWidgets.QPushButton(anaEkran)
        self.sifreGosterButton.setGeometry(QtCore.QRect(290, 80, 121, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sifreGosterButton.sizePolicy().hasHeightForWidth())
        self.sifreGosterButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.sifreGosterButton.setFont(font)
        self.sifreGosterButton.setStyleSheet("background-color: rgb(0, 184, 0);\n"
"alternate-background-color: rgb(0, 225, 0);")
        self.sifreGosterButton.setObjectName("sifreGosterButton")
        self.CozulmusSifreTextBox = QtWidgets.QLabel(anaEkran)
        self.CozulmusSifreTextBox.setGeometry(QtCore.QRect(290, 140, 121, 21))
        self.CozulmusSifreTextBox.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.CozulmusSifreTextBox.setText("")
        self.CozulmusSifreTextBox.setObjectName("CozulmusSifreTextBox")
        self.lineEdit = QtWidgets.QLineEdit(anaEkran)
        self.lineEdit.setGeometry(QtCore.QRect(10, 69, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.textChanged.connect(self.Ara)
        self.lineEdit.setStyleSheet("background-color: rgb(191, 191, 191);")
        self.lineEdit.setObjectName("araTextBox")
        self.loadData()

        self.retranslateUi(anaEkran)
        QtCore.QMetaObject.connectSlotsByName(anaEkran)

    def retranslateUi(self, anaEkran):
        _translate = QtCore.QCoreApplication.translate
        anaEkran.setWindowTitle(_translate("anaEkran", "??ifreler"))
        item = self.sifreTablo.horizontalHeaderItem(0)
        item.setText(_translate("anaEkran", "ID"))
        item = self.sifreTablo.horizontalHeaderItem(1)
        item.setText(_translate("anaEkran", "Uygulama"))
        item = self.sifreTablo.horizontalHeaderItem(2)
        item.setText(_translate("anaEkran", "??ifre"))
        self.cikisButton.setText(_translate("anaEkran", "????k????"))
        self.sifreGosterButton.setText(_translate("anaEkran", "??ifreyi G??ster"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    anaEkran = QtWidgets.QWidget()
    ui = Ui_anaEkran()
    ui.setupUi(anaEkran)
    anaEkran.show()
    sys.exit(app.exec_())
