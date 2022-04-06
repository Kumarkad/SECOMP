class QuadraticProbing:
	def __init__(self):
		self.size=int(input("Enter the size of table : "))
		self.table=list(None for i in range(self.size))
		self.count=0
		self.comparison=0
		
	def isfull(self):
		if self.count==self.size:
			return True
		else:
			return False
		
	# to get hash value
	def hash_function(self,num):
		return num%self.size
		
	def quadraticprobing(self,data):
		i=1
		found =False
		while i <= self.size:
			new_index=(self.hash_function(data[1])+i*i)% self.size
			
			if self.table[new_index] == None:
				found = True
				break
				
			else:
				i +=1
			
		return found,new_index
		
	def insert(self,data):
		
		if self.isfull():
			print("Hash table is full !!!")
			return False
			
		found= False

		index=self.hash_function(data[1])
		
		if self.table[index]==None:
			self.table[index]=data
			print("Phone number of "+str(data[0])+" is placed at position : "+str(index))
			self.count +=1
			
		else:
			print("Collision is occurred for "+str(data[0])+" at position : "+str(index)+"\nFinding new position")
			
			while not found :
				
				found,index = self.quadraticprobing(data)
				
				if found :
					
					self.table[index]= data
					self.count +=1
					print("Phone number of "+str(data[0])+" is placed at position : "+str(index))
					
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
				i=1
				while i<=self.size:
					index=(self.hash_function(data[1])+i*i)% self.size
					
					self.comparison +=1
					
					if self.table[index]==data:
						
						found=True
						break
						
					elif self.table[index] ==None:
						
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
				
		
	def delete(self,data):
		found=False
		index=self.hash_function(data[1])
		
		if self.table[index]!=None:
			
			if self.table[index]==data:
				found=True
				self.table[index]=None
				print("The record deleted successfully !!!")
				return index
			
			else:
				i=1
				while i<=self.size:
					index=(self.hash_function(data[1])+i*i)% self.size
					
					if self.table[index]==data:
						
						self.table[index]=None
						print("The record deleted successfully !!!")
						break
						
					elif self.table[index] ==None:
						
						found=False
						break
						
					else:
						i +=1
						
		else:
			print("Record not Found !!!")
			return found
					
	def display(self):
		print("\n *************Quadratic Probing **********")
		for i in range(self.size):
			if self.table[i] != None:
				data=self.table[i]
				print("Hash Value : "+str(i)+"\t"+"\tName : "+str(data[0])+"\tPhone Number : "+str(data[1]))
			
			else:
					print("Hash Value : "+str(i)+"\t\t"+str(self.table[i]))
					

def input_data():
	data=[]
	name=input("Enter Name : ")
	number=int(input("Enter Number : "))
	data.append(name)
	data.append(number)
	return data

qp=QuadraticProbing()
ch1=0
while ch1 !=5:
	ch1=int(input("""************* Linear Probing ************
	1. Insert
	2. Search
	3. Display
	4. Delete
	5. Back
	Enter your choice : """))
	if ch1==1:
		qp.insert(input_data())
				
	elif ch1==2:
		qp.search(input_data())
				
	elif ch1==3:
		qp.display()
		
	elif ch1==4:
		qp.delete(input_data())
				
	elif ch1>5:
		print("Please enter valid choice !!! ")
				