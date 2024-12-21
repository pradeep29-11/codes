
def fac(num):
	if num==0 or num==1:
		return 1
	else:
		return num*fac(num-1)

num=int(input("Enter the number : "))

ans=fac(num)

print(f"The factoril of : {num} is : {ans}")