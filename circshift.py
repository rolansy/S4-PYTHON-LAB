n=int(input("Enter Number of elements in array : "))
a=[]
b=[]
for i in range(n):
	a.append(int(input("Enter Element : ")))

print("\nInitial Array : ",end="")
for i in a:
	print(i,end=" ")
k=int(input("\nEnter Key  :"))
for i in range(n):
	x=(i-k)%n
	b.append(a[x])

print("\nNew Array : ",end="")
for i in b:
	print(i,end=" ")
print()
