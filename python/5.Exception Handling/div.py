
try:
	a=int(input("Enter first the number : "))
	b=int(input("Enter the second number : "))
	c=a/b
	print(c)

except ZeroDivisionError:
	print("Problem : Denominater is zero")
except ValueError:
	print("Problem : Invalid input !!")
except:
	print("Problem : unknwon error !!")
print("bye")