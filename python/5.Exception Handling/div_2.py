
try:
	a=int(input("Enter first the number : "))
	b=int(input("Enter the second number : "))
	c=a/b

except ZeroDivisionError:
	#print("Problem : Denominater is zero")
	c=a
except ValueError:
	#print("Problem : Invalid input !!")
	c=0
except:
	#print("Problem : unknwon error !!")
	c=0

print("Division : ",c)
print("bye")
