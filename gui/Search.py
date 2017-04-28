# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Search.ui'
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
        self.bar_Search = QtGui.QLineEdit(Form)
        self.bar_Search.setGeometry(QtCore.QRect(30, 60, 371, 31))
        self.bar_Search.setObjectName(_fromUtf8("bar_Search"))
        self.btn_Search = QtGui.QPushButton(Form)
        self.btn_Search.setGeometry(QtCore.QRect(410, 60, 71, 31))
        self.btn_Search.setObjectName(_fromUtf8("btn_Search"))
        self.lbl_Question = QtGui.QLabel(Form)
        self.lbl_Question.setGeometry(QtCore.QRect(150, 20, 181, 16))
        self.lbl_Question.setAutoFillBackground(False)
        self.lbl_Question.setObjectName(_fromUtf8("lbl_Question"))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 110, 191, 201))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.ChoiceGrid_1 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.ChoiceGrid_1.setObjectName(_fromUtf8("ChoiceGrid_1"))
        self.cb_Japanese = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_Japanese.setObjectName(_fromUtf8("cb_Japanese"))
        self.ChoiceGrid_1.addWidget(self.cb_Japanese, 5, 0, 1, 1)
        self.cb_Indonesian = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_Indonesian.setObjectName(_fromUtf8("cb_Indonesian"))
        self.ChoiceGrid_1.addWidget(self.cb_Indonesian, 3, 0, 1, 1)
        self.cb_French = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_French.setObjectName(_fromUtf8("cb_French"))
        self.ChoiceGrid_1.addWidget(self.cb_French, 1, 0, 1, 1)
        self.cb_Chinese = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_Chinese.setObjectName(_fromUtf8("cb_Chinese"))
        self.ChoiceGrid_1.addWidget(self.cb_Chinese, 0, 0, 1, 1)
        self.cb_Indian = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_Indian.setObjectName(_fromUtf8("cb_Indian"))
        self.ChoiceGrid_1.addWidget(self.cb_Indian, 2, 0, 1, 1)
        self.cb_Italian = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_Italian.setObjectName(_fromUtf8("cb_Italian"))
        self.ChoiceGrid_1.addWidget(self.cb_Italian, 4, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(280, 110, 191, 201))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.ChoiceGrid_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.ChoiceGrid_2.setObjectName(_fromUtf8("ChoiceGrid_2"))
        self.cb_Vietnamese = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_Vietnamese.setObjectName(_fromUtf8("cb_Vietnamese"))
        self.ChoiceGrid_2.addWidget(self.cb_Vietnamese, 5, 0, 1, 1)
        self.cb_Taiwanese = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_Taiwanese.setObjectName(_fromUtf8("cb_Taiwanese"))
        self.ChoiceGrid_2.addWidget(self.cb_Taiwanese, 3, 0, 1, 1)
        self.cb_Lebanese = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_Lebanese.setObjectName(_fromUtf8("cb_Lebanese"))
        self.ChoiceGrid_2.addWidget(self.cb_Lebanese, 1, 0, 1, 1)
        self.cb_Korean = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_Korean.setObjectName(_fromUtf8("cb_Korean"))
        self.ChoiceGrid_2.addWidget(self.cb_Korean, 0, 0, 1, 1)
        self.cb_Mexican = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_Mexican.setObjectName(_fromUtf8("cb_Mexican"))
        self.ChoiceGrid_2.addWidget(self.cb_Mexican, 2, 0, 1, 1)
        self.cb_Thai = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_Thai.setObjectName(_fromUtf8("cb_Thai"))
        self.ChoiceGrid_2.addWidget(self.cb_Thai, 4, 0, 1, 1)
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(200, 100, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked()")), self.bar_Search.clear)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Korean.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Lebanese.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Mexican.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Taiwanese.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Thai.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Vietnamese.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Chinese.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_French.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Indian.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Indonesian.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Italian.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Japanese.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Chinese.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_French.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Indian.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Indonesian.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Italian.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Japanese.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Korean.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Lebanese.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Mexican.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Taiwanese.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Thai.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_Vietnamese.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.radioButton.setChecked)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.bar_Search, self.btn_Search)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FoodFinder", None))
        self.btn_Search.setText(_translate("Form", "Search", None))
        self.lbl_Question.setText(_translate("Form", "Where would you like to eat today?", None))
        self.cb_Japanese.setText(_translate("Form", "Japanese", None))
        self.cb_Indonesian.setText(_translate("Form", "Indonesian", None))
        self.cb_French.setText(_translate("Form", "French", None))
        self.cb_Chinese.setText(_translate("Form", "Chinese", None))
        self.cb_Indian.setText(_translate("Form", "Indian", None))
        self.cb_Italian.setText(_translate("Form", "Italian", None))
        self.cb_Vietnamese.setText(_translate("Form", "Vietnamese", None))
        self.cb_Taiwanese.setText(_translate("Form", "Taiwanese", None))
        self.cb_Lebanese.setText(_translate("Form", "Lebanese", None))
        self.cb_Korean.setText(_translate("Form", "Korean", None))
        self.cb_Mexican.setText(_translate("Form", "Mexican", None))
        self.cb_Thai.setText(_translate("Form", "Thai", None))
        self.radioButton.setText(_translate("Form", "All", None))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

