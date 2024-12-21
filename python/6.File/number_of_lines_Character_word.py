
name=input("Enter the file name for read : ")

fr=open(name,"r")

l_count=0
w_count=0
c_count=0

for line in fr:
	l_count=l_count+1
	c_count=c_count+len(line)
	w_count=w_count=len(line.split())

fr.close()
print("The number of line      : ",l_count)
print("The number of word      : ",w_count)
print("The number of character : ",c_count)