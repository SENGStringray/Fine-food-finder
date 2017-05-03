import sys
import re
from PyQt4 import QtCore, QtGui, uic
from Display_Rest_Ui import Ui_WizardPage

class display_restaurant_page(QtGui.QWizardPage, Ui_WizardPage):
	def __init__(self):
		QtGui.QWizardPage.__init__(self)
		self.setupUi(self)
		r_names = ["Cherie-Tree", "Thai-Riffic","Black-Birch"]
		self.get_restaurant_data('Black-Birch', r_names)

	def get_restaurant_data(self, name, restaurant_names):
		if name in restaurant_names: #if restaurant to display is a valid restaurant
			filename = "../Restaurants/%s" % name
			with open(filename) as file:
				for line in file:
					line = re.match( r'^\s*(.+):\s+(.*)$', line, re.M|re.I)
					if line.group(1): 
						label = line.group(1)
					if line.group(2):
						data = line.group(2)
					
					#assign to labels
					if label == 'Name':
						self.restaurantName.setText(data)
					elif label == 'Address':
						self.restaurantAddress.setText(data)
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
						mon = data
					elif label == 'Tuesday':
						tue = data
					elif label == 'Wednesday':
						wed = data
					elif label == 'Thursday':
						thu = data
					elif label == 'Friday':
						fri = data
					elif label == 'Saturday':
						sat = data
					elif label == 'Sunday':
						sun = data
					elif label == 'Price Range':
						priceR = data
					elif label == 'Menu':
						menu = data
					elif label == 'Categories':
						tags = data
			#display error dialog
		else:	
			print "Error: invalid restaurant name"


def main():
	r_names = ["Cherie-Tree", "Thai-Riffic","Black-Birch"]
	app = QtGui.QApplication(sys.argv)
	wiz = display_restaurant_page()
	wiz.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()