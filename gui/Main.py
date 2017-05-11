import sys
import re
import os
import glob
from operator import itemgetter, attrgetter, methodcaller
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import pyqtSlot, SIGNAL, SLOT

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
		self.searchString = ""
		self.checkBoxString = ""

        btn = QtGui.QPushButton('Exit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(50, 30)

		for num in range(0,12):
			checkBox = 'self.cb_' + str(num) + '.stateChanged.connect(self.state_changed' + str(num) + ')'
			exec(checkBox)

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		#fileMenu.addAction(extractAction)

	def handleSearchButton(self):
		#print "Text typed: ", self.searchString
		window.NewSearch = ResultWindow(self.checkBoxString, self.searchString, self)
		self.searchString = ""
		window.NewSearch.show()

	def handleSearchTextChanged(self):
		if (str(self.bar_Search.text()) != ""):
			self.searchString = str(self.bar_Search.text())
		#print "Text bound: ", self.searchString

	def home(self):
		extractAction = QtGui.QAction(QtGui.QIcon('Icon.png'), 'Flee the Scene', self)
		extractAction.triggered.connect(self.close_application)
		self.show()

	def close_application(self):
		#print("Whooaaaa so custome!!!")
		sys.exit()

	def state_changed0(self):
		if (self.cb_0.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_0.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_0.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_0.text(), "")
			elif (self.checkBoxString == str(self.cb_0.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_0.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_0.text(), "")

	def state_changed1(self):
		if (self.cb_1.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_1.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_1.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_1.text(), "")
			elif (self.checkBoxString == str(self.cb_1.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_1.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_1.text(), "")

	def state_changed2(self):
		if (self.cb_2.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_2.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_2.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_2.text(), "")
			elif (self.checkBoxString == str(self.cb_2.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_2.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_2.text(), "")

	def state_changed3(self):
		if (self.cb_3.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_3.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_3.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_3.text(), "")
			elif (self.checkBoxString == str(self.cb_3.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_3.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_3.text(), "")

	def state_changed4(self):
		if (self.cb_4.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_4.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_4.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_4.text(), "")
			elif (self.checkBoxString == str(self.cb_4.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_4.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_4.text(), "")

	def state_changed5(self):
		if (self.cb_5.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_5.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_5.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_5.text(), "")
			elif (self.checkBoxString == str(self.cb_5.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_5.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_5.text(), "")

	def state_changed6(self):
		if (self.cb_6.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_6.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_6.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_6.text(), "")
			elif (self.checkBoxString == str(self.cb_6.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_6.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_6.text(), "")

	def state_changed7(self):
		if (self.cb_7.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_7.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_7.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_7.text(), "")
			elif (self.checkBoxString == str(self.cb_7.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_7.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_7.text(), "")

	def state_changed8(self):
		if (self.cb_8.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_8.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_8.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_8.text(), "")
			elif (self.checkBoxString == str(self.cb_8.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_8.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_8.text(), "")

	def state_changed9(self):
		if (self.cb_9.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_9.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_9.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_9.text(), "")
			elif (self.checkBoxString == str(self.cb_9.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_9.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_9.text(), "")

	def state_changed10(self):
		if (self.cb_10.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_10.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_10.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_10.text(), "")
			elif (self.checkBoxString == str(self.cb_10.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_10.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_10.text(), "")

	def state_changed11(self):
		if (self.cb_11.isChecked()):
			if self.checkBoxString == "":
				self.checkBoxString = str(self.cb_11.text())
			else:
				self.checkBoxString = self.checkBoxString + " " + str(self.cb_11.text())
		else:
			if (self.checkBoxString == ""):
				self.checkBoxString = self.checkBoxString.replace(self.cb_11.text(), "")
			elif (self.checkBoxString == str(self.cb_11.text())):
				  self.checkBoxString = ""
			else:
				self.checkBoxString = self.checkBoxString.replace(self.cb_11.text() + " ", "")
				self.checkBoxString = self.checkBoxString.replace(" " + self.cb_11.text(), "")



class ResultWindow(QtGui.QMainWindow, Ui_MainWindow1):
	def __init__(self, checkBoxStr, searchStr, parent=None):




                #print "Constructing Result window"
		self.searchString = searchStr
		checkBoxStr = re.sub(r'\b(\w+)( \1\b)+', r'\1', checkBoxStr) #Removes repeated words
		#print self.searchString
		#print "String to search: ", self.searchString
		super(ResultWindow, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		self.find_matching_restaurants(searchStr, checkBoxStr)
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


	def find_matching_restaurants(self, searchString, checkboxString):
		print searchString
		print checkboxString
		arrOfRestaurants = []
		path = "../Restaurants/*"
		searchString = searchString.rstrip()
		arrayOfSelectedCat = checkboxString.split() # spilt the checkboxString

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
			m = re.search(r"Price Range:\s*\$([0-9.]+)", content, re.I)
			if (m):
				price = m.group(1)
			else :
				print("ERROR: price not found")
				print(name)
			rest_object = Restaurant(name, price, rating)
			# print rest_object
			#Using the search string to verify the restuarant.
			search_found = 0
			match = re.search(searchString, content, re.I)
			if (match):
				arrOfRestaurants.append(rest_object)
				search_found = 1

			#using the button input to verify the Restaurant.
			for cat in arrayOfSelectedCat:
				cat_match = re.search(r'category:.*?\W', cat)
				if (cat_match and search_found == 0):
					arrOfRestaurants.append(rest_object)
			f.close

		sort_option = "";
		if (sort_option == "price") :
			arrOfRestaurants = sorted(arrOfRestaurants, key=attrgetter('price'))
		elif (sort_option == "name") :
			arrOfRestaurants = sorted(arrOfRestaurants, key=attrgetter('name'))
		else :
			arrOfRestaurants = sorted(arrOfRestaurants, key=attrgetter('rating'))

		for sorted_rest in arrOfRestaurants :
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