

def inputm(r,c):
    l=[]
    for i in range(r):
        col=[]
        for j in range(c):
            y=int(input("Enter Element : "))
            col.append(y)
        l.append(col)
    return l
    
def disp(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j],end= " ")
        print()
        
def addm(a,b):
    x=[]
    for i in range(len(a)):
        col=[]
        for j in range(len(a[i])):
            y=a[i][j]+b[i][j]    
            col.append(y)
        x.append(col)
        
    return x
while True:
    print("\n1Input Matrces\n2.Display  Matrices\n3.Add Matrices\n4.Exit")
    c=int(input("Enter Choice : "))
    if c==1:
        r=int(input("Enter Rows : "))
        c=int(input("Enter COlumns : "))
        a=inputm(r,c)
        b=inputm(r,c)
    elif c==2:
        disp(a)
        disp(b)
    elif c==3:
        x=addm(a,b)
        disp(x)