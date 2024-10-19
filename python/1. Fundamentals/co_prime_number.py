a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

if a<b:
	limit=a 
else:
	limit=b

for i in range(2,limit+1):
	if a%i==0 and b%i==0:
		print(f'{a} and {b} is not co-prime number !')
		break

else:
	print(f'{a} and {b} is a co-prime number !')
