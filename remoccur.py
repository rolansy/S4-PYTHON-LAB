n=int(input("Enter NUmber of elemetns : "))
l=[]

for i in range(n):
	l.append(int(input("Enter Element : ")))
print("Initial Array : ")
for i in l:
	print(i,end=" ")
n=[]
print()
for i in l:
	for x in list(str(i)):
		print(x)
		if int(x) not in n:
			n.append(int(x))
print("New Array : ")
for i in n:
	print(i,end=", ")
print()
