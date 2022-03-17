""" To create ADT that implement the "set" concept. 
a. Add (new Element) -Place a value into the set , b. Remove (element) Remove the 
value 
c. Contains (element) Return true if element is in collection, d. Size () Return number of 
values in collection Iterator () Return an iterator used to loop over collection, e. 
Intersection of two sets , f. Union of two sets, g. Difference between two sets, h. Subse
"""

from setoperation import setExample

s=setExample()

print("------------- Welcome ------------")

def choice(ch):
	if ch==1:
		s.create()
		
	elif ch==2:
		s.insert()
		
	elif ch==3:
		s.remove()
		
	elif ch==4:
		s.search()
		
	elif ch==5:
		s.display()
		
	elif ch==6:
		s.set_union()
		
	elif ch==7:
		s.set_intersection()
		
	elif ch==8:
		s.set_difference()
		
	elif ch==9:
		s.is_subset()
	
	elif ch==10:
		exit("Thank You !!!")
			
	else:
		print("Please enter right choice !!!")
		
while True:
	ch=int(input("""********* Set Operations ********
	1. Create
	2. Insert value in Set
	3. Remove element from Set
	4. Search element in Set
	5. Display Set
	6. Union 
	7. Intersection
	8. Difference
	9. is subset
	10. Exit
	Please enter your choice : """))
	choice(ch)

# Created by : Kumar kad