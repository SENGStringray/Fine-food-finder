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
		self.setStyleSheet("QWidget#Form {background-image: url(bg-1.jpg);border-image:url(bg-1.jpg);background-repeat:no-repeat;}")
		self.view.setStyleSheet("background-color: white; border-radius:4px;")
		self.btn_Search.clicked.connect(self.handleSearchButton)
		self.bar_Search.textChanged.connect(self.handleSearchTextChanged)
		self.bar_Price.textChanged.connect(self.handlePriceTextChanged)
		self.bar_Location.textChanged.connect(self.handleLocationTextChanged)
		self.searchString = ""
		self.priceString = ""
		self.locationString = ""
		self.checkBoxStr = ""
		self.SortedString = "Rating"
		self.ExtraString = "Any"
		self.DietaryString = "Any"
		self.StyleString = "Any"
		self.CuisineString = "Any"
		self.DiningPartyString = "Any"
		self.viewString = "Any" #Default is 'Any'
		self.btn.clicked.connect(self.close_application)

		self.ViewAny.toggled.connect(lambda:self.rbtnState_changed(self.ViewAny))
		self.ViewScenic.toggled.connect(lambda:self.rbtnState_changed(self.ViewScenic))
		self.ViewWaterFront.toggled.connect(lambda:self.rbtnState_changed(self.ViewWaterFront))
		self.ViewBeachFront.toggled.connect(lambda:self.rbtnState_changed(self.ViewBeachFront))

		self.Sorted.currentIndexChanged.connect(self.sortedchange)
		self.Extras.currentIndexChanged.connect(self.Extraschange)
		self.Dietary.currentIndexChanged.connect(self.Dietarychange)
		self.Style.currentIndexChanged.connect(self.Stylechange)
		self.Cuisine.currentIndexChanged.connect(self.Cuisinechange)
		self.DiningParty.currentIndexChanged.connect(self.DiningPartychange)


		#Ensure only numbers are passed into the price box
		regexp = QtCore.QRegExp('^0|[1-9][0-9]{2}$')
		validator = QtGui.QRegExpValidator(regexp)
		self.bar_Price.setValidator(validator)

	def handleSearchButton(self):
		self.checkBoxStr = self.ExtraString + " " + self.DietaryString + " " + self.StyleString + " " + self.CuisineString + " " + self.DiningPartyString + " " + self.viewString;
		window.NewSearch = ResultWindow(self.checkBoxStr, self.SortedString, self.searchString, self.priceString, self.locationString, self)
		self.searchString = ""
		window.NewSearch.show()

	def handleSearchTextChanged(self):
		if (str(self.bar_Search.text()) != ""):
			self.searchString = str(self.bar_Search.text())

	def handlePriceTextChanged(self):
		if (str(self.bar_Price.text()) != ""):
			self.priceString = str(self.bar_Price.text())

	def handleLocationTextChanged(self):
		if (str(self.bar_Location.text()) != ""):
			self.locationString = str(self.bar_Location.text())

	def home(self):
		extractAction = QtGui.QAction(QtGui.QIcon('Icon.png'), 'Flee the Scene', self)
		extractAction.triggered.connect(self.close_application)
		self.show()

	def close_application(self):
		sys.exit()

	def rbtnState_changed(self, button):
		self.viewString = button.text()

	def sortedchange(self,i):
			#print "Items in the list are :"
			#for count in range(self.Sorted.count()):
			#	print self.Sorted.itemText(count)
			#print "Current index",i,"selection changed ",self.Sorted.currentText()
		self.SortedString = self.Sorted.currentText()
		print (self.SortedString)


	def Extraschange(self,i):
		self.ExtraString = self.Extras.currentText()
		print (self.ExtraString)

	def Dietarychange(self,i):
		self.DietaryString = self.Dietary.currentText()
		print (self.DietaryString)
	
	def Stylechange(self,i):
		self.StyleString = self.Style.currentText()
		print (self.StyleString)

	def Cuisinechange(self,i):
		self.CuisineString = self.Cuisine.currentText()
		print (self.CuisineString)
	def DiningPartychange(self,i):
		self.DiningPartyString = self.DiningParty.currentText()
		print (self.DiningPartyString)



class ResultWindow(QtGui.QMainWindow, Ui_MainWindow1):
	def __init__(self, checkBoxStr, SortedString, searchStr, priceStr, locationStr, parent=None):
		super(ResultWindow, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		self.setupUi(self)
		self.find_matching_restaurants(searchStr, checkBoxStr, SortedString, priceStr, locationStr)
		self.resultsList.itemDoubleClicked.connect(self.open_restaurant)
		print ("checkBoxStr: " + checkBoxStr)
		self.btn.clicked.connect(self.close_application)

	def open_restaurant(self, item):
		# print item, str(item.text())
		self.handleRestaurantButton(re.sub(' ', '-',str(item.text())))


	def find_matching_restaurants(self, searchString, checkboxString, sortedString, priceString, locationString):
		print ("searchBox: " + searchString)
		print ("price: " + priceString)
		print ("location: " + locationString)
		print ("checkBoxes: " + checkboxString)
		print ("sort by: " + sortedString)
		
		searchString = str(searchString)
		checkboxString = str(checkboxString)
		locationString = str(locationString)
		priceString = str(priceString)
		sort_option = str(sortedString)
		
		path = "../Restaurants/*"
		searchString = searchString.rstrip()
		locationString = locationString.rstrip()
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
			location_found = 0
			if (search_found == 1) :
				if (locationString == "") :
					location_found = 1
				else :
					match = re.search(locationString, content, re.I)
					if (match):
						location_found = 1
			if (search_found and category_found and location_found) :
				if (priceString != "" and float(rest_object.price) <= float(priceString)):
					arrOfRestaurants.append(rest_object)
				elif (priceString == "") :
					arrOfRestaurants.append(rest_object)

			f.close

			
		sortedList = []
		if (sort_option == "Price") :
			while len(arrOfRestaurants) > 0:
				res = arrOfRestaurants[0]
				for element in arrOfRestaurants :
					if (float(element.price) < float(res.price)) :
						res = element
				sortedList.append(arrOfRestaurants.pop(arrOfRestaurants.index(res)))
		elif (sort_option == "Alphabetical") :
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
					if (float(element.rating) > float(res.rating)) :
						res = element
				sortedList.append(arrOfRestaurants.pop(arrOfRestaurants.index(res)))

		for sorted_rest in sortedList :
			item = QtGui.QListWidgetItem(self.resultsList)
			item.setText(re.sub("-", ' ', sorted_rest.name))
			self.resultsList.addItem(item)

	def handleRestaurantButton(self, name):
		window.NewSearch = RestaurantWindow(self)
		resName = self.sender()
		window.NewSearch.get_restaurant_data(name)
		window.NewSearch.set_res_name(name)
		window.NewSearch.show()


	def close_application(self):
		sys.exit()

class RestaurantWindow(QtGui.QMainWindow, Ui_MainWindow2):
	def __init__(self, parent=None):
		super(RestaurantWindow, self).__init__(parent)
		self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
		QtGui.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		self.setStyleSheet("QWidget#Form {background-image: url(bg-2.jpg);border-image:url(bg-1.jpg);background-repeat:no-repeat;}")
		self.restname = ''
		self.reviewBtn.clicked.connect(lambda: self.append_comment())
		self.btn.clicked.connect(self.close_application)

	def append_comment(self):
		comment = self.usrReview.toPlainText();
		name = self.get_res_name()
		# print name
		# print comment
		filename = "../Restaurants/%s" % name

		with open(filename, 'a') as f:
			f.write(' /' + comment)

	def set_res_name(self, name):
		self.restname = name

	def get_res_name(self):
		return self.restname

	def get_restaurant_data(self, name):
		filename = "../Restaurants/%s" % name
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
					data_new_new = re.sub('-', ' ', data_new)
					self.lbl_restTags.setText(data_new_new)
				elif label == 'Comments':
					data_new = re.sub('^', u"\u2022" + ' ', data)
					data_new_new = re.sub('\s/','\n\n' + u"\u2022" + ' ', data_new)
					self.comments.setText(data_new_new)

	def close_application(self):
			sys.exit()


if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = SearchWindow()
	window.show()
sys.exit(app.exec_())