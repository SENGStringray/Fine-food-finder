import sys
import re
import os
from operator import itemgetter, attrgetter, methodcaller
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
		self.checkBoxString = ""

                btn = QtGui.QPushButton('Exit', self)
                btn.clicked.connect(self.close_application)
                btn.resize(50, 30)

		self.cb_0.stateChanged.connect(self.state_changed0)
		self.cb_1.stateChanged.connect(self.state_changed1)
		self.cb_2.stateChanged.connect(self.state_changed2)
		self.cb_3.stateChanged.connect(self.state_changed3)
		self.cb_4.stateChanged.connect(self.state_changed4)
		self.cb_5.stateChanged.connect(self.state_changed5)
		self.cb_6.stateChanged.connect(self.state_changed6)
		self.cb_7.stateChanged.connect(self.state_changed7)
		self.cb_8.stateChanged.connect(self.state_changed8)
		self.cb_9.stateChanged.connect(self.state_changed9)
		self.cb_10.stateChanged.connect(self.state_changed10)
		self.cb_11.stateChanged.connect(self.state_changed11)

		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		#fileMenu.addAction(extractAction)

	def handleSearchButton(self):
		#print "Text typed: ", self.searchString
		window.NewSearch = ResultWindow(self.checkBoxString, self.searchString, self)
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
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_0.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_0.text())

	def state_changed1(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_1.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_1.text())

	def state_changed2(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_2.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_2.text())

	def state_changed3(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_3.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_3.text())

	def state_changed4(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_4.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_4.text())

	def state_changed5(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_5.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_5.text())

	def state_changed6(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_6.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_6.text())

	def state_changed7(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_7.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_7.text())

	def state_changed8(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_8.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_8.text())

	def state_changed9(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_9.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_9.text())

	def state_changed10(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_10.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_10.text())

	def state_changed11(self):
		if self.checkBoxString == "":
			self.checkBoxString = str(self.cb_11.text())
		else:
			self.checkBoxString = self.checkBoxString + " " + str(self.cb_11.text())




class ResultWindow(QtGui.QMainWindow, Ui_MainWindow1):
	def __init__(self, checkBoxStr, searchStr, parent=None):




                #print "Constructing Result window"
		self.searchString = searchStr
		#print self.searchString
		#print "String to search: ", self.searchString
		super(ResultWindow, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		self.lbl_SearchResult.setText("%s" % searchStr)
		self.lbl_CheckboxResult.setText("%s" % checkBoxStr)
		self.btn_restaurant1.clicked.connect(self.handleRestaurantButton)
		self.btn_restaurant2.clicked.connect(self.handleRestaurantButton)
		self.btn_restaurant3.clicked.connect(self.handleRestaurantButton)
                btn = QtGui.QPushButton('Exit', self)
                btn.clicked.connect(self.close_application)
                btn.resize(50, 30)

	def find_matching_restaurants(self, searchString, checkboxString):
		name = ""
		rating = ""
		price = ""
		arrOfRestaurants = []
		path = "../Restaurants/*"
		searchString = searchString.rstrip()
		arrayOfSelectedCat = []

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
			rest_object = Restuarant(name, price, rating)
			print rest_object
			#Using the search string to verify the restuarant.
			search_found = 0
			match = re.search(searchString, content, re.I)
			if (match):
				arrOfRestuarants.append(rest_object)
				search_found = 1

			#using the button input to verify the Restaurant.
			for cat in arrayOfSelectedCat:
				cat_match = re.search(r'category:.*?\W', cat)
				if (cat_match and search_found == 0):
					arrOfRestuarants.append(rest_object)
			f.close

		sort_option = "";
		if (sort_option == "price") :
			arrOfRestuarants = sorted(arrOfRestuarants, key=attrgetter('price')) 
		elif (sort_option == "name") :
			arrOfRestuarants = sorted(arrOfRestuarants, key=attrgetter('name'))
		else :
			arrOfRestuarants = sorted(arrOfRestuarants, key=attrgetter('rating'))
			
		for sorted_rest in arrOfRestuarants :
			item = QtGui.QListWidgetItem()
			widget = QtGui.QWidget()
			# widget.resize(100, 20)
			# item.setSizeHint(widget.sizeHint())
			widgetName = QtGui.QLabel(name)
			# widgetName = QtGui.QPushButton(name)
			widgetLayout = QtGui.QHBoxLayout()
			widgetLayout.addWidget(widgetName)
			widget.setLayout(widgetLayout)
			self.resultsList.addItem(item)
			self.resultsList.setItemWidget(item, widget)


	def handleRestaurantButton(self):
		window.NewSearch = RestaurantWindow(self)
		resName = self.sender()
		# window.NewSearch.get_restaurant_data(resName.text())
		window.NewSearch.get_restaurant_data('Black-Birch')
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
