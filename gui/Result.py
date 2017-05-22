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
        self.resultsList.setGeometry(QtCore.QRect(20, 80, 761, 521))
        self.resultsList.setMinimumSize(QtCore.QSize(50, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        font.setPointSize(11)
        self.resultsList.setFont(font)
        self.resultsList.setFrameShape(QtGui.QFrame.NoFrame)
        self.resultsList.setResizeMode(QtGui.QListView.Adjust)
        self.resultsList.setObjectName(_fromUtf8("resultsList"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 40, 311, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Sawasdee"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "FoodFinder", None))
        self.label.setText(_translate("Form", "Here is a list of restaurants just for you", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

