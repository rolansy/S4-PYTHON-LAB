#print("largest : ",max(list(map(int,input("Enter three numbers to find largest of : ").split()))))
a=int(input("Enter number A : "))
b=int(input("Enter number B : "))
c=int(input("Enter number C : "))
max=a
if max<b:
	max=b
if max<c:
	max=c
print("Largest of the three numbers is : ",max)
