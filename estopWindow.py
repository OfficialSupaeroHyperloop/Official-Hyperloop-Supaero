# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'estopWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_estopWindow(object):
    def setESTOPstate(self,main_w,MainWindow):
        TextButton= 'ESTOP'
        self.ui=main_w
        self.ui.setupUi(MainWindow)
        self.ui.textBrowser.setText(TextButton)
    def setupUi(self, estopWindow,Ui_MainWindow,MainWindow):
        estopWindow.setObjectName("estopWindow")
        estopWindow.resize(546, 300)
        self.label = QtWidgets.QLabel(estopWindow)
        self.label.setGeometry(QtCore.QRect(150, 80, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.acceptbutton = QtWidgets.QPushButton(estopWindow, clicked=lambda: self.setESTOPstate(Ui_MainWindow,MainWindow))
        self.acceptbutton.clicked.connect(lambda:estopWindow.close())
        self.acceptbutton.setGeometry(QtCore.QRect(170, 200, 93, 28))
        self.acceptbutton.setObjectName("acceptbutton")

        self.declinebutton = QtWidgets.QPushButton(estopWindow)
        self.declinebutton.clicked.connect(lambda:estopWindow.close())

        self.declinebutton = QtWidgets.QPushButton(estopWindow,clicked=lambda:estopWindow.close())

        self.declinebutton.setGeometry(QtCore.QRect(290, 200, 93, 28))
        self.declinebutton.setObjectName("declinebutton")

        self.retranslateUi(estopWindow)
        QtCore.QMetaObject.connectSlotsByName(estopWindow)

    def retranslateUi(self, estopWindow):
        _translate = QtCore.QCoreApplication.translate
        estopWindow.setWindowTitle(_translate("estopWindow", "Dialog"))
        self.label.setText(_translate("estopWindow", "Do you want to proceed? Y/N"))
        self.acceptbutton.setText(_translate("estopWindow", "Yes"))
        self.declinebutton.setText(_translate("estopWindow", "No"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    estopWindow = QtWidgets.QMainWindow()
    ui = Ui_estopWindow()
    ui.setupUi(estopWindow)
    estopWindow.show()

    sys.exit(app.exec_())

    sys.exit(app.exec_())

