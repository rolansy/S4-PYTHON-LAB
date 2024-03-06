a,b=map(int,input("Enter the start and end numbers of the interval : ").split())
print("Prime numbers in the interval",a,"to",b,"are : ",end="")
for i in range(a,b+1):
	f=0
	for j in range(2,i//2+1):
		if i%j==0:
			f=1
			break
	if f==0:
		print(i,end=" ")
print()
