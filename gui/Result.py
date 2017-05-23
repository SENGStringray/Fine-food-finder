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
        Form.resize(800, 620)
        Form.setMinimumSize(QtCore.QSize(800, 620))
        Form.setMaximumSize(QtCore.QSize(800, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.resultsList = QtGui.QListWidget(Form)
        self.resultsList.setGeometry(QtCore.QRect(130, 80, 531, 521))
        self.resultsList.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        font.setPointSize(10)
        self.resultsList.setFont(font)
        self.resultsList.setStyleSheet(_fromUtf8("background:none;padding:5px;text-align:center;"))
        self.resultsList.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultsList.setResizeMode(QtGui.QListView.Adjust)
        self.resultsList.setObjectName(_fromUtf8("resultsList"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 30, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("text-transform:uppercase;color:white;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.btn = QtGui.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(730, 10, 61, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Noto Serif Armenian"))
        font.setBold(True)
        font.setWeight(75)
        self.btn.setFont(font)
        self.btn.setObjectName(_fromUtf8("btn"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FoodFinder", None))
        self.label.setText(_translate("Form", "H e r e  i s   a   l i s t   o f   r e s t a u r a n t s   j u s t   f o r   y o u", None))
        self.btn.setText(_translate("Form", "Close All", None))

