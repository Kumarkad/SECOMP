# program using linear hashing and double hashing

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
	def insert(self,data):
		if self.isfull():
			print("Hash table is full !!!")
			return False

		index=self.hash_function(data[1])
		if self.table[index]==None:
			self.table[index]=data
			print("Phone number of "+str(data[0])+" is placed at position : "+str(index))
			self.count +=1
			
		else:
			print("Collision is occurred for "+str(data[0])+" at position : "+str(index)+"\nFinding new position")
			
			while self.table[index]!=None:
				index +=1
				if index >=self.size:
					index=0
			self.table[index]=data
			print("Phone number of "+str(data[0])+" is placed at position : "+str(index))

			self.count+=1
		return
		
	# to search the data in hash table
	def search(self,data):
		found=False
		index=self.hash_function(data[1])
		self.comparison +=1
		
		if self.table[index]!=None:
			
			if self.table[index]==data:
				found=True
				print("The phone number found at position : "+str(index))
				print("The total comparisons are  : "+str(1))
				return index
			
			else:
				index +=1
			
				if index>=self.size-1:
					index=0
			
				while self.table[index]!=None or self.comparison<=self.size:
				
					if(self.table[index] == data) :
					
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
		print("***********Linear Hashing ************")
		for i in range(self.size):
			if self.table[i] != None:
			    data=self.table[i]
			    print("Hash value : "+str(i)+"\t"+"\t Name : "+str(data[0])+"\t Phone Number : "+str(data[1]))
			
			else:
				print("Hash Value : "+str(i)+"\t\t"+str(self.table[i]))
						

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
	def doublehashing(self,data):
		i=1
		num=data[1]
		found =False
		while i<= self.size:
			new_index=(self.hash1(num)+i*self.hash2(num))%self.size
			
			if self.table[new_index]==None:
				found=True
				break
			
			else:
				i+=1
				
		return found,new_index
			
	#to insert data in  double hashtable
	def insert(self,data):
		
		if self.isfull():
			print("Hash table is full !!!")
			return False
		
		found =False
		
		num=data[1]
		index=self.hash1(num)
		
		if self.table[index]==None:
			self.table[index]=data
			print("Phone number of "+str(data[0])+" is placed at position : "+str(index))
			self.count +=1
			
		else:
			
			print("Collision is occurred for "+str(data[0])+" at position : "+str(index)+"\nFinding new position")
				
			while not found:
				found,index=self.doublehashing(data)
					
				if found:
					self.table[index]=record
						
					self.count+=1
					print("Phone number of "+str(record[0])+" is placed at position : "+str(index))
						
		return found
	
	# search data in double hash table					
	def search(self,data):
		found=False
		index=self.hash1(data[1])
		self.comparison+=1
		
		if self.table[index] !=None:
			if self.table[index]==data :
				found=True
				print("The phone number is found at : "+str(index))
				print("The total number of comparison : "+str(1))
					
			else:
				
				i=1
				while i<=self.size:
					index=(self.hash1(data[1])+i*self.hash2(data[1]))%self.size
					
					self.comparison +=1
					
					if self.table[index]==data:
						
						found=True
						break
						
					elif self.table[index]==None:
						
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
		for i in range(0,self.size):
			if self.table[i] != None :
			    data=self.table[i]
			    print("Hash Value : "+str(i)+"\t Name : "+str(data[0])+"\t Phone Number : "+str(data[1]))
			
			else:
			    print("Hash Value : "+str(i)+"\t"+str(self.table[i]))	
		
											
# accept record from user 			
def input_data():
	data=[]
	name=input("Enter Name : ")
	number=int(input("Enter Number : "))
	data.append(name)
	data.append(number)
	return data
		
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