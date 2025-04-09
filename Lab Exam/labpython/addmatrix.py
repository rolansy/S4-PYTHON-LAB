
def inp(l,r,c):
    l=[]
    for i in range(r):
        x=[]
        for j in range(c):
            x.append(int(input("Enter Element : ")))
        l.append(x)
    return l

def disp(l):
    for i in l:
        for j in i:
            print(j,end=" ")
        print()

def addmat(a,b,r,c):
    x=[]
    for i in range(r):
        y=[]
        for j in range(c):
            y.append(a[i][j]+b[i][j])
        x.append(y)
    return x
            

while True:
    print("\n1.INput Matrices\n2.Display matrices\n3.Add matrices\n4.exit")
    c=int(input("Enter CHoice : "))
    if c==1:
        r=int(input("Enter NUmber of rows : "))
        c=int(input("Enter NUmber of columns : "))
        a=b=[]
        print("Enter matrix a : ")
        a=inp(a,r,c)
        print("Enter matrix b : ")
        b=inp(b,r,c)
    elif c==2:
        print("Matrix a : ")
        disp(a)
        print("Matrix b : ")
        disp(b)
    elif c==3:
        s=[]
        s=addmat(a,b,r,c)
        disp(s)
    elif c==4:
        break
        