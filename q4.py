''' Write a program that asks the user for two numbers. Then ask them if they would like to add, subtract, divide, or multiply these numbers. 
Perform the chosen operation on the values, showing the operation being performed.​
Write four functions, one for each mathematical operation.​
Example: add(), subtract(), Multiply(), and Divide()​ '''
def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def mult(a,b):
	return a*b

def divide(a,b):
	return a/b

more='Y'
while more=='Y' or more=='y':
	print('1. Add')
	print('2. Subtract')
	print('3. Multiply')
	print('4. Divide')
	x = int(input('Your selection : '))
	a,b = list(map(int,input('Enter Numbers : ').split()))
	if x==1:
		print('Result :',add(a,b))
	elif x==2:
		print('Result :',sub(a,b))
	elif x==3:
		print('Result :',mult(a,b))
	elif x==4:
		print('Result :',divide(a,b))
	else:
		print('Enter correct option')
		continue
	more=input('continue y/n : ')