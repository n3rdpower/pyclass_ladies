peanut_butter = int(raw_input("How many servings of peanut butter do you have?  "))
jelly = int(raw_input("How many servings of jelly do you have?  "))
bread_slice = int(raw_input ("How many slices of bread do you have?  "))
bread_serving = bread_slice/2
list1 = (peanut_butter, jelly, bread_serving)

if peanut_butter >= 1 and jelly >= 1 and bread_slice != 0 and bread_slice%2 == 0:
	print "It's Peanut Butter Jelly Time! You have enough servings for {0} sandwiches!".format(min(list1))

elif peanut_butter < 1 and jelly >= 1 and bread_slice != 0 and bread_slice%2 == 0:
	print "you need more peanut butter"

elif peanut_butter >= 1 and jelly < 1 and bread_slice != 0 and bread_slice%2 == 0:
	print "you need more jelly"
	
elif peanut_butter >= 1 and jelly >= 1 and bread_slice >=3 and bread_slice%2==1:
	print "You have an odd number of bread slices, you'll have at least one open faced sandwich"
	
elif peanut_butter >= 1 and jelly >= 1 and bread_slice==1:
	print "You can make an open faced sandwich"

else:
	print "Bottom line: you are simply not prepared for Peanut Butter Jelly Time"
