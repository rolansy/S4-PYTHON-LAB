x=int(input("Enter number to check if armstrong or not : "))
s=0
for i in str(x):
	s+=int(i)**3
if s==x:
	print(x,"is an armstrong number")
else:
	print(x,"is not an armstrong number")
