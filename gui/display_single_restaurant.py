import sys
import re
from PyQt4 import QtCore, QtGui
#Name of restaurant supplied as a STRING

def display_restaurant(name, restaurant_names):
	#find match in array of restaurant names
	if name in restaurant_names: #if restaurant to display is a valid restaurant
		#display page
		filename = "../Restaurants/%s" % name
		#file = open(filename,"r") #read file
		with open(filename) as file:
			for line in file:
				line = re.match( r'^\s*(.+):\s+(.*)$', line, re.M|re.I)
				if line.group(1): 
					key = line.group(1)
				if line.group(2):
					data = line.group(2)
				
				#assign to labels
				if key == 'Name':
					name.setText(data)
				elif key == 'Address':
					print data
				elif key == 'Rating':
					print data
				elif key == 'Monday':
					print data
				elif key == 'Tuesday':
					print data
				elif key == 'Wednesday':
					print data
				elif key == 'Thursday':
					print data
				elif key == 'Friday':
					print data
				elif key == 'Saturday':
					print data
				elif key == 'Sunday':
					print data
				elif key == 'Price Range':
					print data
				elif key == 'Menu':
					print data
				elif key == 'Categories':
					print data
		#display error dialog
	else:	
		print "Error: invalid restaurant name"



r_names = ["Cherie-Tree", "Thai-Riffic","Black-Birch"];
display_restaurant("Thai-Riffic", r_names);
