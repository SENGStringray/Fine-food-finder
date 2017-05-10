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
        self.lbl_Result.setGeometry(QtCore.QRect(80, 0, 71, 20))
        self.lbl_Result.setAutoFillBackground(False)
        self.lbl_Result.setObjectName(_fromUtf8("lbl_Result"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 41, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lbl_Result_2 = QtGui.QLabel(Form)
        self.lbl_Result_2.setGeometry(QtCore.QRect(80, 10, 91, 20))
        self.lbl_Result_2.setAutoFillBackground(False)
        self.lbl_Result_2.setObjectName(_fromUtf8("lbl_Result_2"))
        self.resultsList = QtGui.QListWidget(Form)
        self.resultsList.setGeometry(QtCore.QRect(20, 30, 451, 271))
        self.resultsList.setMinimumSize(QtCore.QSize(50, 20))
        self.resultsList.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultsList.setResizeMode(QtGui.QListView.Adjust)
        self.resultsList.setObjectName(_fromUtf8("resultsList"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FoodFinder", None))
        self.lbl_Result.setText(_translate("Form", "Search result:", None))
        self.pushButton.setText(_translate("Form", "Exit", None))
        self.lbl_Result_2.setText(_translate("Form", "Checkbox result:", None))

