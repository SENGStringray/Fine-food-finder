#!/usr/bin/py

import sys, re, os

searchString = sys.stdin.readline()
searchString.rstrip()
path = "/Users/justindaerolee/School/seng2011/project" # write the path
arrOfRestuarants = []
for fileN in glob.glob(os.path.join(path, '*.txt')): # doesn't seem to work 
	f  = open(fileN, “r”)
	content = f.read()
	match = re.search(searchString, content)
	if (match):
		arrOfRestuarants.apphend(fileN)
	f.close

for fileN in ArrOfRestuarants:
	print(fileN)

class Restuarant:
        def __init__(self, name, price, rating):
                self.name = name
                self.price = price
                self.rating = rating
        def __repr__(self):
                return repr((self.name, self.price, self.rating))
        

sorted(arrOfRestuarants, key=lambda Restuarant: Restuarant.name)

