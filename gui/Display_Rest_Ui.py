# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Display_Rest.ui'
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

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(806, 638)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(WizardPage.sizePolicy().hasHeightForWidth())
        WizardPage.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        font.setPointSize(18)
        font.setItalic(True)
        WizardPage.setFont(font)
        self.restaurantName = QtGui.QLabel(WizardPage)
        self.restaurantName.setGeometry(QtCore.QRect(30, 30, 311, 64))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.restaurantName.setFont(font)
        self.restaurantName.setObjectName(_fromUtf8("restaurantName"))
        self.restaurantAddress = QtGui.QLabel(WizardPage)
        self.restaurantAddress.setGeometry(QtCore.QRect(30, 130, 751, 37))
        self.restaurantAddress.setObjectName(_fromUtf8("restaurantAddress"))
        self.restaurantRating = QtGui.QLabel(WizardPage)
        self.restaurantRating.setGeometry(QtCore.QRect(30, 90, 341, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.restaurantRating.setFont(font)
        self.restaurantRating.setObjectName(_fromUtf8("restaurantRating"))
        self.line = QtGui.QFrame(WizardPage)
        self.line.setGeometry(QtCore.QRect(30, 170, 741, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage", None))
        self.restaurantName.setText(_translate("WizardPage", "Restaurant Name", None))
        self.restaurantAddress.setText(_translate("WizardPage", "Address", None))
        self.restaurantRating.setText(_translate("WizardPage", "Rating", None))

