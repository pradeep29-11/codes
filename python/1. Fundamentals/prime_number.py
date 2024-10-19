num1=int(input("Enter the number : "))

if num1<0:
	print(f'please enter the positive number !')

if num1==1:
	print(f'{num1} is not a prime number !')
	exit(0)

j=0
for i in range(2,num1):
	if num1%i==0:
		j=1
		break
if j==0:
	print(f'{num1} is prime number ')
else:
	print(f'{num1} is not a prime number ')