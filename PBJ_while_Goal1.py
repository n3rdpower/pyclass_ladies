# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

bread = int(raw_input("how many slices of bread do you have?  "))
peanut_butter = int(raw_input("how many servings of peanut butter do you have?  "))
jelly = int(raw_input("how many servings of jelly do you have?  "))
sandwich = []

while bread >=2 and peanut_butter >=1 and jelly >=1:
	sandwich.append('PBJ')
	bread= bread-2
	peanut_butter = peanut_butter-1
	jelly = jelly-1
	
for index, PBJ in enumerate(sandwich):
	print "Making sandwich #{0}".format(index+1)
	
if bread <2 and peanut_butter >=1 and jelly >=1:
	print "All done; only had enough bread for {0} sandwiches.".format(len(sandwich))
	
elif bread >=2 and peanut_butter <=0 and jelly >=1:
	print "All done; only had enough peanut butter for {0} sandwiches.".format(len(sandwich))
	
elif bread >=2 and peanut_butter >=1 and jelly <=0:
	print "All done; only had enough jelly for {0} sandwiches.".format(len(sandwich))
	
elif bread<=0 or peanut_butter==0 or jelly==0:
	print "You only had enough ingredients for {0} sandwiches.".format(len(sandwich))
	
