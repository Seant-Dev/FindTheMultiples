# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator, QRegExpValidator


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(191, 399)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 171, 141))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 151, 104))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 171, 61))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(11, 30, 151, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 171, 25))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 250, 171, 141))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 220, 171, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.pushButton.raise_()
        self.listWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.pushButton.clicked.connect(self.calculo)
        self.pushButton_2.clicked.connect(self.limpiar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multiplos"))
        self.groupBox.setTitle(_translate("MainWindow", "Rango de Busqueda"))
        self.label.setText(_translate("MainWindow", "Menor"))
        self.label_2.setText(_translate("MainWindow", "Mayor"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Numero"))
        self.pushButton.setText(_translate("MainWindow", "Calcular Multiplos"))
        self.pushButton_2.setText(_translate("MainWindow", "Limpiar"))

    def lim_inf(self):
        return self.lineEdit.text()

    def lim_sup(self):
        return self.lineEdit_2.text()

    def numero(self):
        return self.lineEdit_3.text()

    def desactivar_boton(self):
        self.pushButton.setDisabled(True)
        self.pushButton.setHidden(True)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setVisible(True)

    def limpiar(self):
        self.pushButton_2.setDisabled(True)
        self.pushButton_2.setHidden(True)
        self.pushButton.setVisible(True)
        self.pushButton.setEnabled(True)
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.listWidget.clear()

    def calculo(self):
        try:
            lim_inf = int(self.lineEdit.text())
            lim_sup = int(self.lim_sup())
            numero = int(self.numero())
        except ValueError:
            print("Las opciónes que ingreso no son validas")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        else:
            multiplos = []
            if lim_inf <= lim_sup:
                print("Los parametros son validos")
                while lim_inf <= lim_sup:
                    if (lim_inf % numero) == 0:
                        multiplos.append(str(lim_inf))
                        lim_inf = lim_inf + 1
                    else:
                        lim_inf = lim_inf + 1
                self.listWidget.addItems(multiplos)
                self.desactivar_boton()
            else:
                print("Los limites no son validos")
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.lineEdit_3.clear()