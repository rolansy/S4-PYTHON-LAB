s=input("Enter string  : ")
w=input("Enter word to replace : ")
l=s.split(" ")
if w in l:
    x=input("Enter New word  : ")
    l[l.index(w)]=x
else:
    print("w doesnt exist ")

for i in l:
    print(i,end=" ")
