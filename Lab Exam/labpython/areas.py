def tr(l,b):
    print("Area of triangle : ",(l*b)/2)
def rect(l,b):
    print("Area of rect : ",l*b)
c=0
while c!=4:
    print("1.tri\n2.rect\n3input\n4.exit")
    c=int(input("Enter CHoic e : "))
    
    if c==1:
        tr(l,b)
    elif c==2:
        rect(l,b)
    elif c==3:
        l=int(input("Enter Lenght : "))
        b=int(input("Enter brdth : "))
    elif c==4:
        print()
    else:
        print("INvalid")