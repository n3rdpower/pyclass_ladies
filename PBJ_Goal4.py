peanut_butter = int(raw_input("How many servings of peanut butter do you have?  "))
jelly = int(raw_input("How many servings of jelly do you have?  "))
bread_slice = int(raw_input ("How many slices of bread do you have?  "))
bread_serving = bread_slice/2.0
list1 = (peanut_butter, jelly, bread_serving)

if min(list1)==max(list1) and min(list1)!= 0 and bread_slice%2 == 0:
	print "It's Peanut Butter Jellxy Time! You have enough servings for {0} sandwiches!".format(min(list1))

elif jelly<max(list1) or peanut_butter<max(list1) or bread_serving<max(list1) and bread_slice%2==0 and max(list1)!= 0:
	print "you need {0} servings of jelly".format(max(list1)-jelly)
	print "you need {0} servings of peanut butter".format(max(list1)-peanut_butter)
	print "you need {0:.1f} servings of bread".format(max(list1)-bread_serving)
	print "then you will be able to make {0} sandwiches".format(max(list1))
