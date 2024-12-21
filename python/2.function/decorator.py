
def mydecor(f):
	def inner():
		f()
		print("I am red")
	return inner

@mydecor
def display():
	print("I am white")

display()
