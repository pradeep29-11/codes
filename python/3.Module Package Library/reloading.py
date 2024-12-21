import pradeep
from importlib import reload
print("Hii")
print(pradeep.a)

input("Wait for 2 second after press any key ")

reload(pradeep)
print(pradeep.a)