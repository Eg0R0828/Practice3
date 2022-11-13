# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 860)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-6, 0, 1211, 861))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 191, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox {\n"
"background: rgba(200, 200, 200, 220);\n"
"}")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 171, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 171, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 171, 81))
        self.groupBox_2.setObjectName("groupBox_2")
        self.mc = QtWidgets.QLabel(self.groupBox_2)
        self.mc.setGeometry(QtCore.QRect(10, 20, 151, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.mc.setFont(font)
        self.mc.setStyleSheet("QLabel {\n"
"color: rgb(255, 0, 0);\n"
"}")
        self.mc.setTextFormat(QtCore.Qt.PlainText)
        self.mc.setObjectName("mc")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 90, 171, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Circuit Checker"))
        self.groupBox.setTitle(_translate("Dialog", "MENU"))
        self.pushButton_2.setText(_translate("Dialog", "Check the picture"))
        self.groupBox_2.setTitle(_translate("Dialog", "LEGEND"))
        self.mc.setText(_translate("Dialog", "Missing capacitor!"))
        self.pushButton_3.setText(_translate("Dialog", "Update datasets"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
