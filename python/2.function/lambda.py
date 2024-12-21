
def fun(a,b,f):
	x=f(a,b)
	print(f"Maximum number is {x}")


fun(11,9,lambda x,y: x if x>y else y)
