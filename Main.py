import sys
from PyQt4 import QtCore, QtGui, uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("Search.ui")
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType("Result.ui")
Ui_MainWindow2, QtBaseClass2 = uic.loadUiType("Restaurant.ui")

class SearchWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.btn_Search.clicked.connect(self.handleSearchButton)
        self.bar_Search.textChanged.connect(self.handleSearchTextChanged)
        self.searchString = ""

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        #fileMenu.addAction(extractAction)

    def handleSearchButton(self):
        print "Text typed: ", self.searchString
        window.NewSearch = ResultWindow(self.bar_Search.text(), self)
        window.NewSearch.show()

    def handleSearchTextChanged(self):
        self.searchString = str(self.bar_Search.text())
        print "Text bound: ", self.searchString

    def home(self):
        extractAction = QtGui.QAction(QtGui.QIcon('Icon.png'), 'Flee the Scene', self)
        extractAction.triggered.connect(self.close_application)
        self.show()
        
    def close_application(self):
        print("Whooaaaa so custome!!!")
        sys.exit()


        
class ResultWindow(QtGui.QMainWindow, Ui_MainWindow1):
    def __init__(self, searchStr, parent=None):
        print "Constructing Result window"
        print "Search string passed: ", searchStr
        self.searchString = searchStr
        print self.searchString
        super(ResultWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.btn_restaurant1.clicked.connect(self.handleRestaurantButton)
        self.btn_restaurant2.clicked.connect(self.handleRestaurantButton)
        self.btn_restaurant3.clicked.connect(self.handleRestaurantButton)


    def handleRestaurantButton(self):
    	window.NewSearch = RestaurantWindow(self)
    	resName = self.sender()
    	window.NewSearch.lbl_restName.setText("%s" % str(resName.text()))
    	window.NewSearch.show()

class RestaurantWindow(QtGui.QMainWindow, Ui_MainWindow2):
    def __init__(self, parent=None):
        super(RestaurantWindow, self).__init__(parent)
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec_())