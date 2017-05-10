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
        self.lbl_Result.setGeometry(QtCore.QRect(50, 20, 71, 20))
        self.lbl_Result.setAutoFillBackground(False)
        self.lbl_Result.setObjectName(_fromUtf8("lbl_Result"))
        self.btn_restaurant1 = QtGui.QPushButton(Form)
        self.btn_restaurant1.setGeometry(QtCore.QRect(150, 20, 91, 31))
        self.btn_restaurant1.setObjectName(_fromUtf8("btn_restaurant1"))
        self.btn_restaurant2 = QtGui.QPushButton(Form)
        self.btn_restaurant2.setGeometry(QtCore.QRect(140, 50, 91, 31))
        self.btn_restaurant2.setObjectName(_fromUtf8("btn_restaurant2"))
        self.btn_restaurant3 = QtGui.QPushButton(Form)
        self.btn_restaurant3.setGeometry(QtCore.QRect(250, 20, 91, 31))
        self.btn_restaurant3.setObjectName(_fromUtf8("btn_restaurant3"))
        self.lbl_restaurant1 = QtGui.QLabel(Form)
        self.lbl_restaurant1.setGeometry(QtCore.QRect(250, 30, 311, 31))
        self.lbl_restaurant1.setObjectName(_fromUtf8("lbl_restaurant1"))
        self.lbl_restaurant2 = QtGui.QLabel(Form)
        self.lbl_restaurant2.setGeometry(QtCore.QRect(70, 10, 311, 31))
        self.lbl_restaurant2.setObjectName(_fromUtf8("lbl_restaurant2"))
        self.lbl_restaurant3 = QtGui.QLabel(Form)
        self.lbl_restaurant3.setGeometry(QtCore.QRect(190, 60, 311, 31))
        self.lbl_restaurant3.setObjectName(_fromUtf8("lbl_restaurant3"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 41, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lbl_SearchResult = QtGui.QLabel(Form)
        self.lbl_SearchResult.setGeometry(QtCore.QRect(130, 20, 351, 21))
        self.lbl_SearchResult.setAutoFillBackground(False)
        self.lbl_SearchResult.setText(_fromUtf8(""))
        self.lbl_SearchResult.setObjectName(_fromUtf8("lbl_SearchResult"))
        self.lbl_CheckboxResult = QtGui.QLabel(Form)
        self.lbl_CheckboxResult.setGeometry(QtCore.QRect(130, 50, 351, 21))
        self.lbl_CheckboxResult.setAutoFillBackground(False)
        self.lbl_CheckboxResult.setText(_fromUtf8(""))
        self.lbl_CheckboxResult.setObjectName(_fromUtf8("lbl_CheckboxResult"))
        self.lbl_Result_2 = QtGui.QLabel(Form)
        self.lbl_Result_2.setGeometry(QtCore.QRect(40, 50, 91, 20))
        self.lbl_Result_2.setAutoFillBackground(False)
        self.lbl_Result_2.setObjectName(_fromUtf8("lbl_Result_2"))
        self.resultsList = QtGui.QListWidget(Form)
        self.resultsList.setGeometry(QtCore.QRect(20, 100, 451, 201))
        self.resultsList.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultsList.setResizeMode(QtGui.QListView.Adjust)
        self.resultsList.setObjectName(_fromUtf8("resultsList"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FoodFinder", None))
        self.lbl_Result.setText(_translate("Form", "Search result:", None))
        self.btn_restaurant1.setText(_translate("Form", "restaurant 1", None))
        self.btn_restaurant2.setText(_translate("Form", "restaurant 2", None))
        self.btn_restaurant3.setText(_translate("Form", "restaurant 3", None))
        self.lbl_restaurant1.setText(_translate("Form", "Restaurant 1 details", None))
        self.lbl_restaurant2.setText(_translate("Form", "Restaurant 2 details", None))
        self.lbl_restaurant3.setText(_translate("Form", "Restaurant 3 details", None))
        self.pushButton.setText(_translate("Form", "Exit", None))
        self.lbl_Result_2.setText(_translate("Form", "Checkbox result:", None))

