a=int(input("Enter start no. : "))
b=int(input("Enter end no : "))
print("Prime no.s are : ",end="")
for i in range(a,b):
    f=1
    for j in range(2,(i//2)+1):
        if i%j==0:
            f=0
            break
    if f:
        print(i,end=" ")
        