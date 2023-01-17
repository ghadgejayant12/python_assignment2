# Develop a module over datetime library for calculating difference between 2 given time and date.​
# The module that is required is present datediff.py file that module is now called in this .py file
print('Q3 output :')
from datediff import date,time
print('Difference between 2022/12/03 and 2024/08/19 is',date('2024/12/03','2022/08/19'))
print('Difference between 12:08:00 and 9:19:12 is',time('12:08:00','9:19:12'))