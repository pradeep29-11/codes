
def display(End,Start=0):
	i=Start
	while i<End:
		if i%2==0:
			yield i
		i=i+1

ans=display(5)

print(list(ans))
