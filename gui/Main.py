import sys
import re
import os
import glob
from operator import itemgetter, attrgetter, methodcaller
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import pyqtSlot, SIGNAL, SLOT
from PyQt4.QtCore import *
from PyQt4.QtGui import *

Ui_MainWindow, QtBaseClass = uic.loadUiType("Search.ui")
Ui_MainWindow1, QtBaseClass1 = uic.loadUiType("Result.ui")
Ui_MainWindow2, QtBaseClass2 = uic.loadUiType("Restaurant.ui")


class Restaurant:
		def __init__(self, name, price, rating):
				self.name = name
				self.price = price
				self.rating = rating

		def __repr__(self):
				return repr((self.name, self.price, self.rating))

class QCustomQWidget (QtGui.QWidget):
    def __init__ (self, parent = None):
        super(QCustomQWidget, self).__init__(parent)
        self.textQVBoxLayout = QtGui.QVBoxLayout()
        self.textUpQLabel    = QtGui.QLabel()
        # self.textDownQLabel  = QtGui.QLabel()
        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        # self.textQVBoxLayout.addWidget(self.textDownQLabel)
        self.allQHBoxLayout  = QtGui.QHBoxLayout()
        # self.iconQLabel      = QtGui.QLabel()
        # self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 0)
        self.setLayout(self.allQHBoxLayout)
        # setStyleSheet
    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

class SearchWindow(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.btn_Search.clicked.connect(self.handleSearchButton)
		self.bar_Search.textChanged.connect(self.handleSearchTextChanged)
		self.bar_Price.textChanged.connect(self.handlePriceTextChanged)
		self.searchString = ""
		self.priceString = ""
		self.checkBoxString = ""
		self.viewString = "Any" #Default is 'Any'

		btn = QtGui.QPushButton('Exit', self)
		btn.clicked.connect(self.close_application)
		btn.resize(50, 30)






                
		#self.cb_0.stateChanged.connect(lambda:self.cbstate_changed(self.cb_0))
		#self.cb_1.stateChanged.connect(lambda:self.cbstate_changed(self.cb_1))
		#self.cb_2.stateChanged.connect(lambda:self.cbstate_changed(self.cb_2))
		#self.cb_3.stateChanged.connect(lambda:self.cbstate_changed(self.cb_3))
		#self.cb_4.stateChanged.connect(lambda:self.cbstate_changed(self.cb_4))
		#self.cb_5.stateChanged.connect(lambda:self.cbstate_changed(self.cb_5))
		#self.cb_6.stateChanged.connect(lambda:self.cbstate_changed(self.cb_6))
		#self.cb_7.stateChanged.connect(lambda:self.cbstate_changed(self.cb_7))
		#self.cb_8.stateChanged.connect(lambda:self.cbstate_changed(self.cb_8))
		#self.cb_9.stateChanged.connect(lambda:self.cbstate_changed(self.cb_9))
		#self.cb_10.stateChanged.connect(lambda:self.cbstate_changed(self.cb_10))
		#self.cb_11.stateChanged.connect(lambda:self.cbstate_changed(self.cb_11))

		self.rbtn_View_1.toggled.connect(lambda:self.rbtnState_changed(self.rbtn_View_1))
		self.rbtn_View_2.toggled.connect(lambda:self.rbtnState_changed(self.rbtn_View_2))
		self.rbtn_View_3.toggled.connect(lambda:self.rbtnState_changed(self.rbtn_View_3))
		self.rbtn_View_4.toggled.connect(lambda:self.rbtnState_changed(self.rbtn_View_4))

		#Ensure only numbers are passed into the price box
		regexp = QtCore.QRegExp('^0|[1-9][0-9]{2}$')
		validator = QtGui.QRegExpValidator(regexp)
		self.bar_Price.setValidator(validator)

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		#fileMenu.addAction(extractAction)

	def handleSearchButton(self):
		#print "Text typed: ", self.searchString
		window.NewSearch = ResultWindow(self.checkBoxString, self.searchString, self.priceString, self.viewString, self)
		self.searchString = ""
		window.NewSearch.show()

	def handleSearchTextChanged(self):
		if (str(self.bar_Search.text()) != ""):
			self.searchString = str(self.bar_Search.text())
		#print "Text bound: ", self.searchString

	def handlePriceTextChanged(self):
		if (str(self.bar_Price.text()) != ""):
			self.priceString = str(self.bar_Price.text())

	def home(self):
		extractAction = QtGui.QAction(QtGui.QIcon('Icon.png'), 'Flee the Scene', self)
		extractAction.triggered.connect(self.close_application)
		self.show()

	def close_application(self):
		#print("Whooaaaa so custome!!!")
		sys.exit()

	def rbtnState_changed(self, button):
		self.viewString = button.text()

	def cbstate_changed(self, button):
		if (button.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = button.text()
			else:
				self.checkBoxString = self.checkBoxString + " " + button.text()
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(button.text(), "")
			elif (self.checkBoxString == button.text()):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(button.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + button.text(), "")

class ResultWindow(QtGui.QMainWindow, Ui_MainWindow1):
	def __init__(self, checkBoxStr, searchStr, priceStr, viewStr, parent=None):




                #print "Constructing Result window"
		#self.searchString = searchStr
		#self.priceString = priceStr
		#self.viewString = viewStr
		checkBoxStr = re.sub(r'\b(\w+)( \1\b)+', r'\1', checkBoxStr) #Removes repeated words
		#print self.searchString
		#print "String to search: ", self.searchString
		super(ResultWindow, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		self.find_matching_restaurants(searchStr, checkBoxStr, priceStr, viewStr)
		# self.resultsList.currentItemChanged.connect(self.handleRestaurantButton(self.resultsList.current().widget.textUpQLabel))
		# self.resultsList.itemDoubleClicked.connect(self.handleRestaurantButton(self.resultsList.currentItem().text()))
		self.resultsList.itemDoubleClicked.connect(self.open_restaurant)
		# self.lbl_SearchResult.setText("%s" % searchStr)
		# self.lbl_CheckboxResult.setText("%s" % checkBoxStr)
		# self.btn_restaurant1.clicked.connect(self.handleRestaurantButton)
		# self.btn_restaurant2.clicked.connect(self.handleRestaurantButton('Black-Birch'))
		# self.btn_restaurant3.clicked.connect(self.handleRestaurantButton)
                btn = QtGui.QPushButton('Exit', self)
                btn.clicked.connect(self.close_application)
                btn.resize(50, 30)

	def open_restaurant(self, item):
		# print item, str(item.text())
		self.handleRestaurantButton(re.sub(' ', '-',str(item.text())))


	def find_matching_restaurants(self, searchString, checkboxString, priceString, viewString):
		print ("searchBox: " + searchString)
		print ("price: " + priceString)
		print ("checkBoxes: " + checkboxString)
		print ("view: " + viewString)
		sort_option = ""
		
		path = "../Restaurants/*"
		searchString = searchString.rstrip()
		checkboxString = checkboxString.rstrip()
		arrayOfSelectedCat = checkboxString.split() # spilt the checkboxString

		arrOfRestaurants = []
		for fileN in glob.glob(path):
			f  = open(fileN, 'r')
			content = f.read()
			# initialising the Restuarant object
			name = re.sub(r'.*?/', '', fileN)
			m = re.search(r"Rating:\s*([0-9.]+)", content, re.I)
			if (m) :
				rating = m.group(1)
			else :
				print("ERROR: rating not found")
				print(name)
				continue
			m = re.search(r"Price Range:\s*\$([0-9.]+)", content, re.I)
			if (m):
				price = m.group(1)
			else :
				print("ERROR: price not found")
				print(name)
				continue

			rest_object = Restaurant(name, price, rating)
			# searching based on checkbox String
			# intersection of checked boxes

			## change the category cause the category is changing
			category_found = 1
			if (checkboxString != "") :
				for cat in arrayOfSelectedCat:
					# category is changed into different categories fix this.
					cat_match = re.search(cat, content, re.I)
					if (cat_match== None):
						category_found = 0
						break
			#Using the search string to verify the restuarant.
			search_found = 0
			if (category_found == 1) :
				if (searchString == "") :
					search_found = 1
				else :
					match = re.search(searchString, content, re.I)
					if (match):
						search_found = 1
			if (search_found and category_found) :
                if (priceString != "") :
                    if (float(priceString) >= rest_object.price) :
                        arrOfRestaurants.append(rest_object)
                else :
                    arrOfRestaurants.append(rest_object)

			f.close
			
		sortedList = []
		if (sort_option == "price") :
			while len(arrOfRestaurants) > 0:
				res = arrOfRestaurants[0]
				for element in arrOfRestaurants :
					if (float(element.price) < float(res.price)) :
						res = element
				sortedList.append(arrOfRestaurants.pop(arrOfRestaurants.index(res)))
		elif (sort_option == "name") :
			while len(arrOfRestaurants) > 0:
				res = arrOfRestaurants[0]
				for element in arrOfRestaurants :
					if (element.name < res.name) :
						res = element
				sortedList.append(arrOfRestaurants.pop(arrOfRestaurants.index(res)))
		else :
			while len(arrOfRestaurants) > 0:
				res = arrOfRestaurants[0]
				for element in arrOfRestaurants :
					if (float(element.rating) < float(res.rating)) :
						res = element
				sortedList.append(arrOfRestaurants.pop(arrOfRestaurants.index(res)))

		for sorted_rest in sortedList :
			# widget = QCustomQWidget()
			# widget.setTextUp(sorted_rest.name)
			# widget.setTextDown(sorted_rest.price)
			item = QtGui.QListWidgetItem(self.resultsList)
			item.setText(re.sub("-", ' ', sorted_rest.name))
			# item.setSizeHint(widget.sizeHint())
			self.resultsList.addItem(item)
			# self.resultsList.setItemWidget(item, widget)

	def handleRestaurantButton(self, name):
		window.NewSearch = RestaurantWindow(self)
		resName = self.sender()
		# window.NewSearch.get_restaurant_data(resName.text())
		window.NewSearch.get_restaurant_data(name)
		# window.NewSearch.lbl_restName.setText("%s" % str(resName.text()))
		window.NewSearch.show()


	def close_application(self):
		sys.exit()

class RestaurantWindow(QtGui.QMainWindow, Ui_MainWindow2):
	def __init__(self, parent=None):
		super(RestaurantWindow, self).__init__(parent)
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)

	def get_restaurant_data(self, name):
		filename = "../Restaurants/%s" % name
		# print "%s" %
		with open(filename) as file:
			for line in file:
				line = re.match( r'^\s*(.+):\s+(.*)$', line, re.M|re.I)
				if line.group(1):
					label = line.group(1)
				if line.group(2):
					data = line.group(2)
				if label == 'Name':
					self.lbl_restName.setText(data)
				elif label == 'Address':
					self.lbl_restAddress.setText(data)
				elif label == 'Rating':
					stars = round(float(data))
					no_stars = 5 - round(float(data))
					string = ""
					while stars > 0:
						string += u"\u272f"
						stars = stars - 1
					while no_stars > 0:
						string += u"\u2606"
						no_stars = no_stars-1
					self.restaurantRating.setText(string)
				elif label == 'Monday':
					self.tradingHours.addItem("Monday: " + data)
				elif label == 'Tuesday':
					self.tradingHours.addItem("Tuesday: " + data)
				elif label == 'Wednesday':
					self.tradingHours.addItem("Wednesday: " + data)
				elif label == 'Thursday':
					self.tradingHours.addItem("Thursday: " + data)
				elif label == 'Friday':
					self.tradingHours.addItem("Friday: " + data)
				elif label == 'Saturday':
					self.tradingHours.addItem("Saturday: " + data)
				elif label == 'Sunday':
					self.tradingHours.addItem("Sunday: " + data)
				elif label == 'Price Range':
					priceR = data
				elif label == 'Menu':
					data_new = re.sub(',\s', '\n', data)
					self.lbl_restMenu.setText(data_new)
				elif label == 'Categories':
					data_new = re.sub(',\s', '\n', data)
					self.lbl_restTags.setText(data_new)

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = SearchWindow()
	window.show()
	sys.exit(app.exec_())
