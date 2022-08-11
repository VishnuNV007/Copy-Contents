#Python program to copy the contents of a file to another file 
with open('python1.txt','r') as firstfile, open('abc.txt','a') as secondfile:
	
	
	for line in firstfile:
			secondfile.write(line)
