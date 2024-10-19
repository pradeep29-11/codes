"""
def add_number(a,b):
	c=a+b
	print(f"Sum of two number is {c}")

x=int(input("Enter the first number : "))
y=int(input("Enter the second number : "))

add_number(x,y)

def subtract_number(x,y):
	return x-y

x=int(input("Enter the first number : "))
y=int(input("Enter the second number : "))

z=subtract_number(x,y)
print(f"Subtraction of {x} and {y} is {z}")


def additon(num):
	if num:
		return num+additon(num-1)
	else:
		return 0
a=int(input("Enter the  number : "))

z=additon(a)
print(f"Sum of number : {z}")


def pradeep(x):
	print(f"The name is {x}")

z=input("Enter the name : ")
aniket=pradeep
aniket(z)
"""
x=int(input("Enter the first number : "))
print(list(range(4,x, 2)))