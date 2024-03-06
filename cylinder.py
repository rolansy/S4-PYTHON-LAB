import math

r=int(input("Enter radius : "))
l=int(input("Enter Height : "))
def sa(r,l):
	s=math.pi*r*((2*r)+l)
	print("Surface Area : ",s)
def v(r,l):
	x=math.pi*r*r*l
	print("Volume : ",x)
c=0
while(c!=3):
	print("\n1.Surface Area\n2.Volume\n3.Exit\n")
	c=int(input("Enter Choice : "))
	if c==1:
		sa(r,l)
	elif c==2:
		v(r,l)
	elif c!=3:
		print("Invalid Choice")
