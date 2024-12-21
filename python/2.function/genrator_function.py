def display():
	yield "hello"
	yield "Bye"

G=display()

print(type(G))

for data in G:
	print(data)