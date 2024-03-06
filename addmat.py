

def disp(l):
	for i in l:
		for j in  i:
			print(j,end=" ")
		print()
	print()

def inputm(l,r,c):
	l=[]
	for i in range(r):
		rw=[]
		for j in range(c):
			rw.append(int(input("Enter Element : ")))
		l.append(rw)
	return l

def addm(a,b):
	c=[]
	for i in range(len(a)):
		x=[]
		for j in range(len(a[i])):
			x.append(a[i][j]+b[i][j])
		c.append(x)
	return c

while True:
	print("\n1.Input mAtrices \n2.display matrices\n3.Add matrices\n4.Exit ")
	c=int(input("Enter Choice : "))
	if c==1:
		r=int(input("Enter Number of rows : "))
		c=int(input("Enter Number of COlumns : "))
		a=b=[]
		print("Enter Matrix A : ")
		a=inputm(a,r,c)
		print("Enter Matrix B : ")
		b=inputm(b,r,c)
	elif c==2:
		print("Matrix A : ")
		disp(a)
		print("\nMatrix B : ")
		disp(b)
	elif c==3:
		r=[]
		r=addm(a,b)
		print("Resultant Matrix : ")
		disp(r)
	else:
		break
		
		
		
	
