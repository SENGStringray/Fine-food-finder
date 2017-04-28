import sys
from PyQt4 import QtCore, QtGui, uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("Search.ui")
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType("Result.ui")

class SearchWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Search.clicked.connect(self.handleSearchButton)

    def handleSearchButton(self):
        window.NewSearch = ResultWindow(self)
        window.NewSearch.show()


class ResultWindow(QtGui.QMainWindow, Ui_MainWindow1):
    def __init__(self, parent=None):
        super(ResultWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())