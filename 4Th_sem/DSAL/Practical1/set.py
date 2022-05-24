""" To create ADT that implement the "set" concept. 
a. Add (new Element) -Place a value into the set , b. Remove (element) Remove the 
value 
c. Contains (element) Return true if element is in collection, d. Size () Return number of 
values in collection Iterator () Return an iterator used to loop over collection, e. 
Intersection of two sets , f. Union of two sets, g. Difference between two sets, h. Subse
"""
class setExample:
	set1=set()
	set2=set()
	
	def create(self):
		set1=self.set1
		num=int(input("Enter the number do you want insert in set 1 : "))
		for i in range(0,num):
			val=input("Enter the value : ")
			set1.add(val)
		
	def insert(self):
		set1=self.set1
		val=input("Enter the value to insert in Set 1 : ")
		set1.add(val)
		
	def remove(self):
		set1=self.set1
		val=input('Enter the value to remove from Set 1 : ')
		
		if val not in set1:
		    print("Value not found in Set 1 !!!")
		else:
		    set1.discard(val)
		    print("Value removed successfully ")
		
	def search(self):
		set1=self.set1
		val=input('Enter the value to search in Set 1 : ')
		key=None
		for i in set1:
			if i==val:
				key=True
				
		if key==True:
			print("Value is found in Set")
		else:
			print("Value is not found is Set !!!")
		
	def set_union(self):
		set1=self.set1
		set2=self.set2
		num=int(input("Enter the number do you want insert in set 2 : "))
		for i in range(0,num):
			val=input("Enter the value : ")
			set2.add(val)
		set3=set1.union(set2)
		print("Union of set1 and set2 is : ",set3)
		
	def set_intersection(self):
		set1=self.set1
		set2=self.set2
		num=int(input("Enter the number do you want insert in set 2 : "))
		for i in range(0,num):
			val=input("Enter the value : ")
			set2.add(val)
		set3=set1.intersection(set2)
		print("Intersection of set1 and set2 is : ",set3)
		
	def set_difference(self):
		set1=self.set1
		set2=self.set2
		num=int(input("Enter the number do you want insert in set 2 : "))
		for i in range(0,num):
			val=input("Enter the value : ")
			set2.add(val)
		set3=set1.difference(set2)
		print("Difference of set1 and set2 is : ",set3)
		
	def is_subset(self):
		set1=self.set1
		val=[val for val in input("Enter the subset : ").split()]
		sets=set(val)
		res =sets.issubset(set1)
		if res==True:
			print("This is subset of set1")
		else:
			print("This is not subset of set1")
		
	def display(self):
		set1=self.set1
		print("set1: ",set1)
		
	def size_of_set(self):
		print("Size of set 1 is : ",self.set1.__len__())
		
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
	    s.size_of_set()
	    
	elif ch==11:
		exit("Thank You !!!")
			
	else:
		print("Please enter right choice !!!")
		
while True:
	ch=int(input("""********* Set Operations ********
	1. Create
	2. Insert value in Set 1
	3. Remove element from Set 1
	4. Search element in Set 1
	5. Display Set 1
	6. Union 
	7. Intersection
	8. Difference
	9. is subset
	10. print size of set 1
	11. Exit
	Please enter your choice : """))
	choice(ch)

# Created by : Kumar kad