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
        self.bar_Search.setGeometry(QtCore.QRect(30, 50, 371, 31))
        self.bar_Search.setObjectName(_fromUtf8("bar_Search"))
        self.btn_Search = QtGui.QPushButton(Form)
        self.btn_Search.setGeometry(QtCore.QRect(410, 50, 71, 31))
        self.btn_Search.setObjectName(_fromUtf8("btn_Search"))
        self.lbl_Question = QtGui.QLabel(Form)
        self.lbl_Question.setGeometry(QtCore.QRect(130, 20, 251, 16))
        self.lbl_Question.setAutoFillBackground(False)
        self.lbl_Question.setObjectName(_fromUtf8("lbl_Question"))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 110, 191, 201))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.ChoiceGrid_1 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.ChoiceGrid_1.setObjectName(_fromUtf8("ChoiceGrid_1"))
        self.cb_5 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_5.setObjectName(_fromUtf8("cb_5"))
        self.ChoiceGrid_1.addWidget(self.cb_5, 5, 0, 1, 1)
        self.cb_3 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_3.setObjectName(_fromUtf8("cb_3"))
        self.ChoiceGrid_1.addWidget(self.cb_3, 3, 0, 1, 1)
        self.cb_1 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_1.setObjectName(_fromUtf8("cb_1"))
        self.ChoiceGrid_1.addWidget(self.cb_1, 1, 0, 1, 1)
        self.cb_0 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_0.setObjectName(_fromUtf8("cb_0"))
        self.ChoiceGrid_1.addWidget(self.cb_0, 0, 0, 1, 1)
        self.cb_2 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_2.setObjectName(_fromUtf8("cb_2"))
        self.ChoiceGrid_1.addWidget(self.cb_2, 2, 0, 1, 1)
        self.cb_4 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_4.setObjectName(_fromUtf8("cb_4"))
        self.ChoiceGrid_1.addWidget(self.cb_4, 4, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(280, 110, 191, 201))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.ChoiceGrid_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.ChoiceGrid_2.setObjectName(_fromUtf8("ChoiceGrid_2"))
        self.cb_11 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_11.setObjectName(_fromUtf8("cb_11"))
        self.ChoiceGrid_2.addWidget(self.cb_11, 5, 0, 1, 1)
        self.cb_9 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_9.setObjectName(_fromUtf8("cb_9"))
        self.ChoiceGrid_2.addWidget(self.cb_9, 3, 0, 1, 1)
        self.cb_6 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_6.setObjectName(_fromUtf8("cb_6"))
        self.ChoiceGrid_2.addWidget(self.cb_6, 0, 0, 1, 1)
        self.cb_8 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_8.setObjectName(_fromUtf8("cb_8"))
        self.ChoiceGrid_2.addWidget(self.cb_8, 2, 0, 1, 1)
        self.cb_10 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_10.setObjectName(_fromUtf8("cb_10"))
        self.ChoiceGrid_2.addWidget(self.cb_10, 4, 0, 1, 1)
        self.cb_7 = QtGui.QCheckBox(self.gridLayoutWidget_2)
        self.cb_7.setObjectName(_fromUtf8("cb_7"))
        self.ChoiceGrid_2.addWidget(self.cb_7, 1, 0, 1, 1)
        self.radioButton = QtGui.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(220, 90, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 41, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_6.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_7.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_8.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_9.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_10.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_11.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_0.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_1.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_2.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_3.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_4.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_5.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_0.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_1.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.cb_2.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_3.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_4.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_5.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_6.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_7.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_8.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_9.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_10.setChecked)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_11.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.radioButton.setChecked)
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("released()")), self.bar_Search.undo)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.bar_Search, self.btn_Search)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FoodFinder", None))
        self.btn_Search.setText(_translate("Form", "Search", None))
        self.lbl_Question.setText(_translate("Form", "Where would you like to eat today?", None))
        self.cb_5.setText(_translate("Form", "Japanese", None))
        self.cb_3.setText(_translate("Form", "Indonesian", None))
        self.cb_1.setText(_translate("Form", "French", None))
        self.cb_0.setText(_translate("Form", "Chinese", None))
        self.cb_2.setText(_translate("Form", "Indian", None))
        self.cb_4.setText(_translate("Form", "Italian", None))
        self.cb_11.setText(_translate("Form", "Vietnamese", None))
        self.cb_9.setText(_translate("Form", "Taiwanese", None))
        self.cb_6.setText(_translate("Form", "Korean", None))
        self.cb_8.setText(_translate("Form", "Mexican", None))
        self.cb_10.setText(_translate("Form", "Thai", None))
        self.cb_7.setText(_translate("Form", "Lebanese", None))
        self.radioButton.setText(_translate("Form", "All", None))
        self.pushButton.setText(_translate("Form", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

