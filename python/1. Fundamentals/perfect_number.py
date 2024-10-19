num=int(input("Enter the number : "))

data=0
for i in range(1,num):
	if num%i==0:
		data=data+i

if data==num:
	print(f'{num} is the perfect number !')
else:
	print(f'{num} is not a perfect number !')
	