def display(End,Start=0):
	i=Start
	while i<End:
		yield i
		i=i+1

ans=display(Start=0,End=6)

for i in ans:
 	print(i)
