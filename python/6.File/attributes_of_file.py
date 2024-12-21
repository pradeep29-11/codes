
fw=open("a.txt","w")

fw.write("I love India")
print("File name -->",fw.name)
print("File mode -->",fw.mode)
print("Readable --->",fw.readable())
print("Writable -->",fw.writable())
print("Susesfully put data in file")

fw.close()
print("File close-->",fw.closed)
