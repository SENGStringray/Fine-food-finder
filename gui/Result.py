# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Result.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(500, 320)
        Form.setMinimumSize(QtCore.QSize(500, 320))
        Form.setMaximumSize(QtCore.QSize(500, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.lbl_Result = QtGui.QLabel(Form)
        self.lbl_Result.setGeometry(QtCore.QRect(230, 20, 41, 16))
        self.lbl_Result.setAutoFillBackground(False)
        self.lbl_Result.setObjectName(_fromUtf8("lbl_Result"))
        self.btn_restaurant1 = QtGui.QPushButton(Form)
        self.btn_restaurant1.setGeometry(QtCore.QRect(40, 50, 91, 31))
        self.btn_restaurant1.setObjectName(_fromUtf8("btn_restaurant1"))
        self.btn_restaurant2 = QtGui.QPushButton(Form)
        self.btn_restaurant2.setGeometry(QtCore.QRect(40, 110, 91, 31))
        self.btn_restaurant2.setObjectName(_fromUtf8("btn_restaurant2"))
        self.btn_restaurant3 = QtGui.QPushButton(Form)
        self.btn_restaurant3.setGeometry(QtCore.QRect(40, 170, 91, 31))
        self.btn_restaurant3.setObjectName(_fromUtf8("btn_restaurant3"))
        self.lbl_restaurant1 = QtGui.QLabel(Form)
        self.lbl_restaurant1.setGeometry(QtCore.QRect(170, 50, 311, 31))
        self.lbl_restaurant1.setObjectName(_fromUtf8("lbl_restaurant1"))
        self.lbl_restaurant2 = QtGui.QLabel(Form)
        self.lbl_restaurant2.setGeometry(QtCore.QRect(170, 110, 311, 31))
        self.lbl_restaurant2.setObjectName(_fromUtf8("lbl_restaurant2"))
        self.lbl_restaurant3 = QtGui.QLabel(Form)
        self.lbl_restaurant3.setGeometry(QtCore.QRect(170, 170, 311, 31))
        self.lbl_restaurant3.setObjectName(_fromUtf8("lbl_restaurant3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FoodFinder", None))
        self.lbl_Result.setText(_translate("Form", "Result", None))
        self.btn_restaurant1.setText(_translate("Form", "restaurant 1", None))
        self.btn_restaurant2.setText(_translate("Form", "restaurant 2", None))
        self.btn_restaurant3.setText(_translate("Form", "restaurant 3", None))
        self.lbl_restaurant1.setText(_translate("Form", "Restaurant 1 details", None))
        self.lbl_restaurant2.setText(_translate("Form", "Restaurant 2 details", None))
        self.lbl_restaurant3.setText(_translate("Form", "Restaurant 3 details", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

