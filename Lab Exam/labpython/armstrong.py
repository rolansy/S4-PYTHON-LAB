n=int(input("Enter Number to check armstrong or not : "))
x=0
for i in str(n):
    x+=int(i)**3
if x==n:
    print(n," is an arstromg no")
else:
    print(n," is not an arstromg no")