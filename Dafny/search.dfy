class restaurant{
	var name: real, price: real, rating: rating
	require fileN != null
	new arr0Restaurants[]
	Method print(){Enter search String}
	Method sys.stdin.readline(){return searchString;}
	Method print(){Enter search String}
	Method searchString.rstrip(){return ;}
	Method print(){Enter search categories, or press cntrl+d}
	forall fileN{
		Method open(){ return f;}
		Method f.read{return content;}
		Method re.search(searchString, content){return match;}
		if match then   Method arrOfRestuarants.apphend(fileN){return ;} else Mehtod close()
	}
	for fileN | fileN in ArrOfRestuarants{
		Method print(fileN){return ;}
	}


	if sort_option = "price" {Method sorted(arrOfRestuarants, key=lambda Restuarant: Restuarant.name)}
	elsif sort_option = "price"{Method sorted(arrOfRestuarants, key=lambda Restuarant: Restuarant.price)}
	else {Method sorted(arrOfRestuarants, key=lambda Restuarant: Restuarant.rating)}
	forall rest | arrOfRestuarants {Method print() {print rest.name} }

}
