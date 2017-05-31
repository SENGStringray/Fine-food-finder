method sorted(a: array <char>,key :int,priceA:int,priceB:int) returns (i: int,j:int)
requires a != null
//ensures 0 <= i ==> i < a.Length
//ensures 0 <= j ==> j > 0
{	
 // var j :int;
  var sort_option: string;
  var element: char;
  var res: char;
  //var priceA: int;
  //var priceB: int;
  j:=a.Length;
  i:=0;
	if sort_option == "price" {
		while j > 0 
    {
			res := a[0];
			while i < a.Length
       // invariant  0 <= i <= a.Length
      {
				if priceA < priceB {
					res := element;
				}
				i:=i+1;
			}
      j := j - 1;
		}
	}
}
