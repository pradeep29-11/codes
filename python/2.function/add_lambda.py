def fun(a,b,f):
	x=f(a,b)
	print(f"Addition of two number is {x}")

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))

fun(a,b,lambda x,y:x+y)
