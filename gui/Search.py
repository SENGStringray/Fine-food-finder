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
        Form.setEnabled(True)
        Form.resize(800, 620)
        Form.setMinimumSize(QtCore.QSize(800, 620))
        Form.setMaximumSize(QtCore.QSize(800, 620))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.bar_Search = QtGui.QLineEdit(Form)
        self.bar_Search.setGeometry(QtCore.QRect(200, 440, 371, 31))
        self.bar_Search.setObjectName(_fromUtf8("bar_Search"))
        self.btn_Search = QtGui.QPushButton(Form)
        self.btn_Search.setGeometry(QtCore.QRect(340, 510, 71, 31))
        self.btn_Search.setObjectName(_fromUtf8("btn_Search"))
        self.lbl_Question = QtGui.QLabel(Form)
        self.lbl_Question.setGeometry(QtCore.QRect(250, 10, 271, 61))
        self.lbl_Question.setAutoFillBackground(False)
        self.lbl_Question.setObjectName(_fromUtf8("lbl_Question"))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(600, 280, 191, 201))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.ChoiceGrid_1 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.ChoiceGrid_1.setObjectName(_fromUtf8("ChoiceGrid_1"))
        self.cb_3 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_3.setObjectName(_fromUtf8("cb_3"))
        self.ChoiceGrid_1.addWidget(self.cb_3, 4, 0, 1, 1)
        self.cb_1 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_1.setObjectName(_fromUtf8("cb_1"))
        self.ChoiceGrid_1.addWidget(self.cb_1, 2, 0, 1, 1)
        self.cb_0 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_0.setObjectName(_fromUtf8("cb_0"))
        self.ChoiceGrid_1.addWidget(self.cb_0, 0, 0, 1, 1)
        self.cb_4 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_4.setObjectName(_fromUtf8("cb_4"))
        self.ChoiceGrid_1.addWidget(self.cb_4, 5, 0, 1, 1)
        self.cb_2 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_2.setObjectName(_fromUtf8("cb_2"))
        self.ChoiceGrid_1.addWidget(self.cb_2, 3, 0, 1, 1)
        self.cb_5 = QtGui.QCheckBox(self.gridLayoutWidget)
        self.cb_5.setObjectName(_fromUtf8("cb_5"))
        self.ChoiceGrid_1.addWidget(self.cb_5, 1, 0, 1, 1)
        self.gridLayoutWidget_2 = QtGui.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(600, 70, 191, 201))
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
        self.radioButton.setGeometry(QtCore.QRect(660, 510, 82, 17))
        self.radioButton.setAutoExclusive(False)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 41, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.Tourist = QtGui.QFontComboBox(Form)
        self.Tourist.setGeometry(QtCore.QRect(200, 80, 371, 31))
        self.Tourist.setObjectName(_fromUtf8("Tourist"))
        self.style = QtGui.QFontComboBox(Form)
        self.style.setGeometry(QtCore.QRect(200, 180, 371, 31))
        self.style.setObjectName(_fromUtf8("style"))
        self.bar_Price = QtGui.QLineEdit(Form)
        self.bar_Price.setGeometry(QtCore.QRect(200, 390, 371, 31))
        self.bar_Price.setObjectName(_fromUtf8("bar_Price"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 380, 61, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 80, 68, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 180, 51, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 420, 151, 31))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.fontComboBox = QtGui.QFontComboBox(Form)
        self.fontComboBox.setGeometry(QtCore.QRect(200, 130, 371, 27))
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(100, 130, 68, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 240, 68, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.Diatary = QtGui.QFontComboBox(Form)
        self.Diatary.setGeometry(QtCore.QRect(200, 230, 371, 31))
        self.Diatary.setObjectName(_fromUtf8("Diatary"))
        self.Extras = QtGui.QFontComboBox(Form)
        self.Extras.setGeometry(QtCore.QRect(200, 280, 371, 31))
        self.Extras.setObjectName(_fromUtf8("Extras"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(100, 290, 68, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.rbtn_View_3 = QtGui.QRadioButton(Form)
        self.rbtn_View_3.setGeometry(QtCore.QRect(370, 330, 91, 22))
        self.rbtn_View_3.setObjectName(_fromUtf8("rbtn_View_3"))
        self.rbtn_View_4 = QtGui.QRadioButton(Form)
        self.rbtn_View_4.setGeometry(QtCore.QRect(480, 330, 91, 22))
        self.rbtn_View_4.setObjectName(_fromUtf8("rbtn_View_4"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(100, 330, 68, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.rbtn_View_1 = QtGui.QRadioButton(Form)
        self.rbtn_View_1.setGeometry(QtCore.QRect(200, 330, 51, 22))
        self.rbtn_View_1.setChecked(True)
        self.rbtn_View_1.setObjectName(_fromUtf8("rbtn_View_1"))
        self.rbtn_View_2 = QtGui.QRadioButton(Form)
        self.rbtn_View_2.setGeometry(QtCore.QRect(280, 330, 71, 22))
        self.rbtn_View_2.setObjectName(_fromUtf8("rbtn_View_2"))

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
        QtCore.QObject.connect(self.btn_Search, QtCore.SIGNAL(_fromUtf8("released()")), self.bar_Price.clear)
        QtCore.QObject.connect(self.radioButton, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.cb_2.setChecked)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.bar_Search, self.btn_Search)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FoodFinder", None))
        self.btn_Search.setText(_translate("Form", "Search", None))
        self.lbl_Question.setText(_translate("Form", "Where would you like to eat today?", None))
        self.cb_3.setText(_translate("Form", "Indonesian", None))
        self.cb_1.setText(_translate("Form", "French", None))
        self.cb_0.setText(_translate("Form", "Chinese", None))
        self.cb_4.setText(_translate("Form", "Italian", None))
        self.cb_2.setText(_translate("Form", "Indian", None))
        self.cb_5.setText(_translate("Form", "Japanese", None))
        self.cb_11.setText(_translate("Form", "Vietnamese", None))
        self.cb_9.setText(_translate("Form", "Taiwanese", None))
        self.cb_6.setText(_translate("Form", "Korean", None))
        self.cb_8.setText(_translate("Form", "Mexican", None))
        self.cb_10.setText(_translate("Form", "Thai", None))
        self.cb_7.setText(_translate("Form", "Lebanese", None))
        self.radioButton.setText(_translate("Form", "All", None))
        self.pushButton.setText(_translate("Form", "Exit", None))
        self.label.setText(_translate("Form", "Price:", None))
        self.label_2.setText(_translate("Form", "Tourist", None))
        self.label_3.setText(_translate("Form", "style", None))
        self.label_4.setText(_translate("Form", "Restaurant Name:", None))
        self.label_5.setText(_translate("Form", "TextLabel", None))
        self.label_6.setText(_translate("Form", "Dietary", None))
        self.label_7.setText(_translate("Form", "Extras", None))
        self.rbtn_View_3.setText(_translate("Form", "Water Front", None))
        self.rbtn_View_4.setText(_translate("Form", "Beach Front", None))
        self.label_8.setText(_translate("Form", "View", None))
        self.rbtn_View_1.setText(_translate("Form", "Any", None))
        self.rbtn_View_2.setText(_translate("Form", "Scenic", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

