# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Restaurant.ui'
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
        Form.setMinimumSize(QtCore.QSize(500, 316))
        Form.setMaximumSize(QtCore.QSize(500, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.lbl_restName = QtGui.QLabel(Form)
        self.lbl_restName.setGeometry(QtCore.QRect(50, 30, 371, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_restName.setFont(font)
        self.lbl_restName.setText(_fromUtf8(""))
        self.lbl_restName.setObjectName(_fromUtf8("lbl_restName"))
        self.lbl_restDetails = QtGui.QLabel(Form)
        self.lbl_restDetails.setGeometry(QtCore.QRect(50, 90, 411, 171))
        self.lbl_restDetails.setTextFormat(QtCore.Qt.PlainText)
        self.lbl_restDetails.setObjectName(_fromUtf8("lbl_restDetails"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FoodFinder", None))
        self.lbl_restDetails.setText(_translate("Form", "Restaurant details", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

