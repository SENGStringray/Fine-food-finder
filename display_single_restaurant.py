import sys
from PyQt4 import QtCore, QtGui
#Name of restaurant supplied as a STRING

	def display_restaurant(name, restaurant_names):
		#find match in array of restaurant names
		if name in restaurant_names:
			#display page
			filename = "restaurants/%s" % name
			file = open(filename,"r") #read file
			print file.read()
		else:
			break;
			#display error dialog
			print "Error: invalid restaurant name"