''' Create a file hash.txt with some content. Append '#' to every next character and display the content on screen.​
Example :​
If the file hash.txt has the following content stored in it :​
THE WORLD IS NOT FLAT​

Your code should display the following content :​
T#H#E# #W#O#R#L#D# #I#S# #N#O#T# F#L#A#T#

'''
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