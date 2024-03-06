c=0
a=int(input("Enter number A : "))
b=int(input("Enter number B : "))

while(c!=5):
	print("1.Add\n2.Subtract\n3.Divide\n4.Multiply\n5.Exit")
	c=int(input("Enter Choice : "))
	if c==1:
		print("Sum : ",a+b)
	elif c==2:
		print("Difference : ",a-b)
	elif c==3:
		print("Quotient : ",a/b)
	elif c==4:
		print("Product : ",a*b)
	elif c==5:
		continue
	else:
		print("Invalid Choice ")
