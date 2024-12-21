import functools
L=[11,22,33,44,55]

x=functools.reduce(lambda x,y:x+y,L)

print(x)
