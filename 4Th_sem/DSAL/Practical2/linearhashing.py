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
				
	def delete(self,data):
		found = False
		index = self.hash_function(data[1])
		self.comparison +=1
		
		if self.table[index] != None:
			
			if self.table[index] == data:
				found=True
				self.table[index] = None
				print("The record deleted successfully !!!")
				return index
			
			else:
				index +=1
			
				if index>=self.size-1:
					index = 0
			
				while self.table[index]!=None or self.comparison<=self.size:
				
					if(self.table[index] == data) :
					
						self.comparison+=1
						found=True
						self.table[index]=None
						print("The record deleted successfully !!!")

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

# accept record from user 			
def input_data():
	data=[]
	name=input("Enter Name : ")
	number=int(input("Enter Number : "))
	data.append(name)
	data.append(number)
	return data
	
lp=LinearProbing()
ch1=0
while ch1 !=5:
	ch1=int(input("""************* Linear Probing ************
	1. Insert
	2. Search
	3. Display
	4. Delete
	5. Exit
	Enter your choice : """))
	if ch1==1:
		lp.insert(input_data())
	elif ch1==2:
		lp.search(input_data())
	elif ch1==3:
		lp.display()
	elif ch1==4:
		lp.delete(input_data())
	elif ch1>5:
		print("Please enter valid choice !!! ")		