#L=input("Enter the list : ")
#L=list(L.split())

L=[1,2,3,4,5,6,7]
vals=filter(lambda x:x%2==0,L)

even_list=list(vals)
print(even_list)