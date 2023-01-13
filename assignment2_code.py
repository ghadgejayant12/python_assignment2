from pprint import pprint
def read_csv(dtype):
	file = open('data.csv','r')
	fh = file.readlines()
	fh = [str(i).split(',') for i in fh]
	if dtype=='list':
		return fh[1:]
	if dtype=='dict':
		heads=fh[0]
		ans=dict()
		for i in range(1,len(fh)):
			ans[i]=dict()
			for j in range(len(heads)):
				ans[i][heads[j]]=fh[i][j]
		return ans
	if dtype=='set':
		ans=set()
		for i in fh[1:]:
			ans.add(tuple(i))
		return ans
print('Q1 output :')
print('The CSV file converted to a dictionary :',read_csv('dict'),'\n')
print('The CSV file converted to a list :',read_csv('list'),'\n')
print('The CSV file converted to a set :',read_csv('set'),'\n')

print('---------------------------------------------------------------------------------------')
#---------------------------
#Q2

args = [[1,0],[1,2],[6,3],[1,"a"]]

def handle(num1,num2):
	ans=None
	try:
		ans=num1/num2
		print('Successful division of 2 numbers answer is :',ans)
	except ZeroDivisionError:
		print('You are dividing by zero')
	except TypeError:
		print('The one variable does not contain a number')
	finally:
		return ans
print('O2 Output :')
for i,j in args:
	print('Result :',i,j)
	print("Ans :",handle(i,j))
print('---------------------------------------------------------------------------------------')
#---------------------------------------------------------------
#Q3

print('Q3 output :')
from datediff import date,time
print('Difference between 2022/12/03 and 2024/08/19 is',date('2024/12/03','2022/08/19'))
print('Difference between 12:08:00 and 9:19:12 is',time('12:08:00','9:19:12'))
print('------------------------------------------------------------------------------------')
#-------------------------------------------------------------
#Q4
print('Q4 Output :')
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

#-------------------------------------------------------------------
#Q5
print('-------------------------------------------------')
print('Q5 Output ')
text = input('Enter the  text that must be added in filehash.txt : ')
file = open('filehash.txt','a')
print('Writing text to filehash.txt')
file.write(text)
file.close()
print('Now reading all the data from filehash.txt')
file2=open('filehash.txt','r')
st1 = ''
st2= ''
for line in file2:
	for i in line:
		st1=st1+str(i)+'#'
	st2=st2+str(line)
print('Normal Contents :',st2)
print('Hash Appended Contents :',st1)