t=o=e=to=te=()
n=int(input("Enter Number of elements : "))
for i in range(n):
	t+=int(input("Enter Element : ")),
print(t)
for i in range(n):
	if i%2==0:
		te+=t[i],
	else:
		to+=t[i],
	if t[i]%2==0:
		e+=t[i],
	else: o+=t[i],
print("Even Tuple: ",e)
print("Odd Tuple: ",o)
print("Even Position Tuple: ",te)
print("Odd Position Tuple: ",to)
