# program using linear hashing and double hashing

class Record:
	def __init__(self):
		self.name=None
		self.number=None
		
	def get_name(self):
		return self.name
		
	def get_number(self):
		return self.number
		
	def set_name(self,name):
		self.name=name
		
	def set_number(self,number):
		self.number=number
		
	def __str__(self):
		record="\tName : "+str(self.get_name())+"\t"+"Number : "+str(self.get_number())
		return record

class DoubleHashing:
	
	def __init__(self):
		
		self.size=int(input("Enter the size of table : "))
		self.table=list(None for i in range(self.size))
		self.count=0
		self.comparison=0
		
	# to check whether table is full or not	
	def isfull(self):
		if self.count==self.size:
			return True
		else:
			return False
		
	# to get hash value
	def hash1(self,num):
		return num%self.size
		
	#to get 2nd hash value
	def hash2(self,num):
		return 7-(num%7)
		
	# to generate new hash index
	def doublehashing(self,record):
		i=1
		found =False
		while i<= self.size:
			new_index=(self.hash1(record.get_number())+i*self.hash2(record.get_number()))%self.size
			
			if self.table[new_index]==None:
				found=True
				break
			
			else:
				i+=1
				
		return found,new_index
			
	#to insert data in  double hashtable
	def insert(self,record):
		
		if self.isfull():
			print("Hash table is full !!!")
			return False
		
		found =False

		index=self.hash1(record.get_number())
		
		if self.table[index]==None:
			self.table[index]=record
			print("Phone number of "+record.get_name()+" is placed at position : "+str(index))
			self.count +=1
			
		else:
			
			print("Collision is occurred for "+record.get_name()+" at position : "+str(index)+"\nFinding new position")
				
			while not found:
				found,index=self.doublehashing(record)
					
				if found:
					self.table[index]=record
						
					self.count+=1
					print("Phone number of "+record.get_name()+" is placed at position : "+str(index))
						
		return found
	
	# search data in double hash table					
	def search(self,record):
		found=False
		index=self.hash1(record.get_number())
		self.comparison+=1
		
		if self.table[index] !=None:
			if self.table[index].get_name() ==record.get_name() and self.table[index].get_number()==record.get_number():
				found=True
				print("The phone number is found at : "+str(index))
				print("The total number of comparison : "+str(1))
					
			else:
				
				i=1
				while i<=self.size:
					index=(self.hash1(record.get_number())+i*self.hash2(record.get_number()))%self.size
					
					self.comparison +=1
					
					if self.table[index].get_name()==record.get_name() and self.table[index].get_number()==record.get_number():
						
						found=True
						break
						
					elif self.table[index].get_name()==None:
						
						found=False
						break
						
					else:
						i +=1
						
			
				if found:
					print("The phone number is found at : "+str(index))
					print("The total number of comparison : "+str(self.comparison))
				
		else:
			print("Record not Found !!!")
			return found
				
			
	# display double hashtable			
	def display(self):
		print("\n *************Double Hashing **********")
		for i in range(self.size):
			print("Hash Value : "+str(i)+"\t"+str(self.table[i]))	
		
		
class LinearProbing:
	
	# creating constructor of class
	def __init__(self):
		self.size=int(input("Enter the size of table : "))
		self.table=list(None for i in range(self.size))
		self.count=0
		self.comparison=0
	
	# to check whether table is full or not	
	def isfull(self):
		if self.count==self.size:
			return True
		else:
			return False
	
	# to get the hash value	
	def hash_function(self,num):
		return num%self.size
		
	#to insert record in hash table
	def insert(self,record):
		if self.isfull():
			print("Hash table is full !!!")
			return False

		index=self.hash_function(record.get_number())
		if self.table[index]==None:
			self.table[index]=record
			print("Phone number of "+record.get_name()+" is placed at position : "+str(index))
			self.count +=1
			
		else:
			print("Collision is occurred for "+record.get_name()+" at position : "+str(index)+"\nFinding new position")
			
			while self.table[index]!=None:
				index +=1
				if index >=self.size:
					index=0
			self.table[index]=record
			print("Phone number of "+record.get_name()+" is placed at position : "+str(index))

			self.count+=1
		return
		
	# to search the data in hash table
	def search(self,record):
		found=False
		index=self.hash_function(record.get_number())
		self.comparison +=1
		
		if self.table[index]!=None:
			
			if self.table[index].get_name()==record.get_name() and self.table[index].get_number()==record.get_number():
				found=True
				print("The phone number found at position : "+str(index))
				print("The total comparisons are  : "+str(1))
				return index
			
			else:
				index +=1
			
				if index>=self.size-1:
					index=0
			
				while self.table[index]!=None or self.comparison<=self.size:
				
					if(self.table[index].get_name() == record.get_name() and self.table[index].get_number()==record.get_number()):
					
						self.comparison+=1
						found=True
						print("The phone number found at position : "+str(index))
						print("The total comparisons are  : "+str(self.comparison))
						return index
					
					index +=1
				
					if index>=self.size-1:
						index=0
					self.comparison+=1
				
		if  found==False:
				print("Record not Found !!!")
				return False		
		
	# function to display record with hash value
	def display(self):
		print("***********Linear Probing ************")
		for i in range(self.size):
			print("Hash value : "+str(i)+"\t"+str(self.table[i]))
												
# accept record from user 			
def input_data():
	record=Record()
	name=input("Enter Name : ")
	number=int(input("Enter Number : "))
	record.set_name(name)
	record.set_number(number)
	return record
		
ch=0
		
while ch!=3:
	ch=int(input("""**************Hashing************
	1. Linear Probing
	2. Double Hashing
	3. Exit
	Enter your choice : 	"""))
	
	if ch==1:
		lp=LinearProbing()
		ch1=0
		while ch1 !=4:
			
			ch1=int(input("""************* Linear Probing ************
	1. Insert
	2. Search
	3. Display
	4. Back
	Enter your choice : """))
			
			if ch1==1:
				lp.insert(input_data())
				
			elif ch1==2:
				lp.search(input_data())
				
			elif ch1==3:
				lp.display()
				
			elif ch1>4:
				print("Please enter valid choice !!! ")
				
	elif ch==2:
			ch2=0
			dh=DoubleHashing()
			while ch2 !=4:
				ch2=int(input("""************* Double Hashing ************	
	1. Insert
	2. Search
	3. Display
	4. Back
	Enter your choice : """))
				if ch2==1:
					dh.insert(input_data())
				
				elif ch2==2:
					dh.search(input_data())
				
				elif ch2==3:
					dh.display()
				
				elif ch2>4:
					print("Please enter valid choice !!!")
					
# Created by :- Kumar kad