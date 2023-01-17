#Create a function to division by provided argos: [[1, 0], [1, 2], [6, 3], [1, “a”] handle with specific errors
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
	print('Arguments that are to be divided :',i,j)
	print("Ans :",handle(i,j))