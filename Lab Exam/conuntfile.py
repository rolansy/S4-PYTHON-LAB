f1=open("file1.txt","r")
f2=open("file2.txt","w")
l=f1.readlines()
print(l)

nl=len(l)
wc=0
cc=0
d={'u':0,'l':0,'s':0}
for i in l:
    w=i.split()
    wc+=len(w)
    for j in w:
        cc+=len(j)
        for x in j:
            if x.isupper():
                d['u']+=1
            elif x.islower():
                d['l']+=1
            elif not x.isalnum():
                d['s']+=1
            if x.isalnum():
                f2.write(x)
        f2.write(" ")
    f2.write("\n")
f1.close()
f2.close()
        
        
