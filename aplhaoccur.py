import os.path
filename="demo.txt"
counts=[0]*26

def countLetters(line,count_list):
	for letters in line:
		if letters.isalpha():
			count_list[ ord(letters) - ord('a')] +=1
			
if os.path.isfile(filename):
	f= open(filename,'r')
	for line in f:
		countLetters(line.lower(), counts)
		
	for i in range(26):
		print(chr(ord('a')+i),":",str(counts[i]))
else:
	print("File doesn't exists")