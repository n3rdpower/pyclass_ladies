#Basics for Exercise 1

peanut_butter = 2
jelly = 2	
bread_slice = 0

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
