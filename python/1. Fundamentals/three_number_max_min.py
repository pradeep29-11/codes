num1=int(input("Enter the first number  : "))
num2=int(input("Enter the second number : "))
num3=int(input("Enter the third number  : "))

if num1==num2 and num2==num3:
	print("Three number are the Equal !!")
elif num1>num2 and num1>num3:
	print(f'{num1} is greter then {num2} and {num3}')
elif num2>num3:
	print(f'{num2} is greter then {num1} and {num3}')
else:
	print(f'{num3} is greter the {num1} and {num2}')
