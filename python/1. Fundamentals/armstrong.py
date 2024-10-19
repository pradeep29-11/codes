num=int(input("Enter the number : "))

tnum=num
sum=0
while num>0:
	rem=num%10
	sum=sum+(rem**3)
	num=num//10

if sum==tnum:
	print(f'{tnum} is the armstrong number')
else:
	print(f'{tnum} is not a armstrong number')

