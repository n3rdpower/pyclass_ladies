# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

bread = int(raw_input("how many slices of bread do you have?  "))
bread_serving = bread/2
peanut_butter = int(raw_input("how many servings of peanut butter do you have?  "))
jelly = int(raw_input("how many servings of jelly do you have?  "))
sandwich = []

while bread_serving >=1 and peanut_butter !=0 and jelly !=0:
	sandwich.append('PBJ')
	bread= bread-2
	peanut_butter = peanut_butter-1
	jelly = jelly-1
	print "Making sandwich #{0}".format(len(sandwich))
	print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format(bread/2,peanut_butter,jelly)    
		
if jelly == 0:
	print "All done; I ran out of jelly."

elif bread == 0 or bread == 1:
	print "All done; I ran out of bread."

elif peanut_butter == 0:
	print "All done; I ran out of peanut_butter."

else:
	print "All done."
