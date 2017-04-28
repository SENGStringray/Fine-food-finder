import sys
from PyQt4 import QtCore, QtGui
#Name of restaurant supplied as a STRING

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
def display_restaurant(name, restaurant_names):
	#find match in array of restaurant names
	if name in restaurant_names:
		#display page
		filename = "Restaurants/%s" % name
		#file = open(filename,"r") #read file
		with open(filename) as file:
			for line in file:
				name = re.match( r'^Name:\s(.+)$', line, re.M|re.I)
				address = re.match( r'^Address:\s(.+)$', line, re.M|re.I)
				rating = re.match( r'^Rating:\s(.+)$', line, re.M|re.I)
				trading_hours = 
				menu = 
				price_range =
				categories =
				# tags =
				#to connect with GUI -- assign variable to label
				if name: print name.group(1)
				if address: print address.group(1)
				if rating: print rating.group(1)
	else:
		#display error dialog
		print "Error: invalid restaurant name"


r_names = ["Cherie-Tree", "Thai-Riffic"];
display_restaurant("Thai-Riffic", r_names);
=======
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
			print "Error: invalid restaurant name"
=======
			print "Error: invalid restaurant name"
>>>>>>> parent of 8747a9c... update to include restaurant folder
>>>>>>> Stashed changes
