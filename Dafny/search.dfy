 method Search ()
{  
 var content: seq<int>;
 var name: int;
 var rating: int;
 var price: int;
 assume name in content;
  while (name != content[0])
  invariant name in content;
  decreases |content|
  {
    content := content[1..]; 
  }
  assert name==content[0];
   assume rating in content;
  while (rating != content[0])
  invariant rating in content;
  decreases |content|
  {
    content := content[1..]; 
  }
  assert rating==content[0];
  assume price in content;
  while (price != content[0])
  invariant price in content;
  decreases |content|
  {
    content := content[1..]; 
  }
  assert price==content[0];

}