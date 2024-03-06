f=open("file1.txt","r")
d={'U':0,'L':0,'SP':0}
l=f.readlines()
lc=len(l)
wc=0
for i in l:
    a=i.split()
    for x in a:
        if not x.isnumeric():
                wc+=1
        for j in x:
            if j.isupper():
                d['U']+=1
            elif j.islower():
                d['L']+=1
            elif not j.isalnum():
                d['SP']+=1
print("Line Count:",lc)
print("Word Count:",wc)
print("Upper Case Count:",d['U'])
print("Lower Case Count:",d['L'])
print("Special Character Count:",d['SP'])
f.close()
