
str=input("Enter the file to read : ")

fw=open(str,"r")

cnt=0
while True:
	data=fw.read(1)

	if data=="":
		break
	cnt=cnt+1

print("The no of character : ",cnt)
