print("Matrix A : ")
def disp(l):
	for i in l:
		for j in  i:
			print(j,end=" ")
		print()
	print()

def inputm(l,rs,r):
	l=[]
	rs=[]
	for i in range(r):
		rw=[]
		for j in range(r):
			rw.append(int(input("Enter Element : ")))
		l.append(rw)
		rwt=tuple(rw)
		rwtl=list(rwt)
		rwtl.append(sum(rw))
		rs.append(rwtl)
	#rs.append([0]*(len(rwtl)-1))
	return l,rs

r=int(input("Enter Number of rows and Columns : "))
a=b=[]
print("Input elements : ")
a,b=inputm(a,b,r)
print(a)
print("\n",b)
print("A")
disp(a)
print("X")

s=0
x=[0]*r
for i in range(r):
	for j in range (r):
		x[j]+=a[i][j]
		if i==j:
			s+=a[i][j]
b.append(x)
b[len(b)-1].append(s)

disp(b)
