#Basics for Exercise 1

peanut_butter = int(raw_input("How many servings of peanut butter do you have?  "))
jelly = int(raw_input("How many servings of jelly do you have?  "))
bread_slice = int(raw_input ("How many slices of bread do you have?  "))

if peanut_butter >= 1 and jelly >= 1 and bread_slice >= 2:
	print "It's Peanut Butter Jelly Time!"

elif peanut_butter < 1 and jelly >= 1 and bread_slice >= 2:
	print "you need more peanut butter"

elif jelly < 1 and peanut_butter >= 1 and bread_slice >= 2:
	print "you need more jelly"
	
elif bread_slice < 2 and jelly >= 1 and peanut_butter >= 1:
	print "you need more bread to make a decent PB&J"

else:
	print "Bottom line: you are simply not prepared for Peanut Butter Jelly Time"
