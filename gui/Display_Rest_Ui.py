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
        WizardPage.resize(787, 612)
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
        WizardPage.setMouseTracking(False)
        WizardPage.setAcceptDrops(False)
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
        self.line.setGeometry(QtCore.QRect(30, 200, 731, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.widget = QtGui.QWidget(WizardPage)
        self.widget.setGeometry(QtCore.QRect(30, 220, 181, 401))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.widget.setFont(font)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tags = QtGui.QTextEdit(self.widget)
        self.tags.setGeometry(QtCore.QRect(0, 40, 181, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.tags.setFont(font)
        self.tags.setFrameShape(QtGui.QFrame.HLine)
        self.tags.setFrameShadow(QtGui.QFrame.Plain)
        self.tags.setReadOnly(True)
        self.tags.setOverwriteMode(True)
        self.tags.setAcceptRichText(True)
        self.tags.setObjectName(_fromUtf8("tags"))
        self.widget_2 = QtGui.QWidget(WizardPage)
        self.widget_2.setGeometry(QtCore.QRect(220, 220, 541, 401))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.label_2 = QtGui.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.menu = QtGui.QTextEdit(self.widget_2)
        self.menu.setGeometry(QtCore.QRect(0, 40, 541, 321))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(False)
        self.menu.setFont(font)
        self.menu.setFrameShape(QtGui.QFrame.VLine)
        self.menu.setFrameShadow(QtGui.QFrame.Plain)
        self.menu.setReadOnly(True)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.tradingHours = QtGui.QComboBox(WizardPage)
        self.tradingHours.setGeometry(QtCore.QRect(30, 170, 411, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.tradingHours.setFont(font)
        self.tradingHours.setObjectName(_fromUtf8("tradingHours"))
        self.tradingHours.addItem(_fromUtf8(""))

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage", None))
        self.restaurantName.setText(_translate("WizardPage", "Restaurant Name", None))
        self.restaurantAddress.setText(_translate("WizardPage", "Address", None))
        self.restaurantRating.setText(_translate("WizardPage", "Rating", None))
        self.label.setText(_translate("WizardPage", "Features:", None))
        self.label_2.setText(_translate("WizardPage", "Menu", None))
        self.tradingHours.setItemText(0, _translate("WizardPage", "Trading Hours", None))

