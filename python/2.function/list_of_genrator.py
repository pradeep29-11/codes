
def display(End,Start=0):
	i=Start
	while i<End:
		yield i
		i=i+1

ans=display(5)

print(list(ans))