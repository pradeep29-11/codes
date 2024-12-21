
fr=open("a.txt","r")

d={'a':0,'e':0,'i':0,'o':0,'u':0}
while True:
	ch=fr.read(1)
	if ch=="":
		break
	if ch.lower() in d:
		d[ch]=d[ch]+1

print(d)

fr.close()