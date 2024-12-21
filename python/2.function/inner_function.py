def display():
	print("I am in display")
	def fun():
		print("I am in inner function")
	return fun

i=display()
i()