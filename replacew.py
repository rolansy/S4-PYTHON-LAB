s=input("Enter String : ")
a=s.split(" ")
w=input("Enter word r to replace : ")
print("Number of words in string : ",len(a))
if w not in a:
	print(w,"Not found")
else:
	x=a.index(w)
	n=input("Enter New word : ")
	a[x]=n
	for i in a:
		print(i,end=" ")
print()
	


	
