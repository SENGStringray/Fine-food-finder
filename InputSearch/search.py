#!/usr/bin/py

import sys, re, glob

class Restuarant:
        def __init__(self, name, price, rating):
                self.name = name
                self.price = price
                self.rating = rating

        def __repr__(self):
                return repr((self.name, self.price, self.rating))

#search string and category button input uses stdin
#change accordingly later
searchString = sys.stdin.readline()
for line in sys.stdin.readline():
	line.rstrip()
	arrayOfSelectedCat.append(line)
#

searchString = searchString.rstrip()
arrayOfSelectedCat = []
#path = "/Users/justindaerolee/School/seng2011/project/rest" # write the path
#path = path + "/*.txt"
path = "../Restaurants/*.txt"
arrOfRestuarants = []
for fileN in glob.glob(path): 
	f  = open(fileN, 'r')
	content = f.read()
	# initialising the Restuarant object
	name = re.sub(r'.txt$', "", fileN)
	name = re.sub(r'.*/', '', name)
	m = re.search(r"Rating:\s?([0-9.]+)", content)
	if (m) :
		rating = m.group(1)
	else :
		print("ERROR: rating not found")
	m = re.search(r"Price Range:\s?\$([0-9.]+)", content)
	if (m):
		price = m.group(1)
	else :
		print("ERROR: price not found")
	rest_object = Restuarant(name, price, rating)

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

# printing all results.
print("sort by ? name, price or rating")
sort_option = sys.stdin.readline()
if (sort_option == "price") :
	sorted(arrOfRestuarants, key=lambda Restuarant: Restuarant.name)
elif (sort_option = "price") :
	sorted(arrOfRestuarants, key=lambda Restuarant: Restuarant.price)
else :
	sorted(arrOfRestuarants, key=lambda Restuarant: Restuarant.rating)
for rest in arrOfRestuarants:
	print rest.name
# proving sorted and glob.glob function in dafny is going to be a pain
         
