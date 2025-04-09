d={}
while True:
    
    print("\n1.Add Stock\n2.Update Stock\n3.Delete Stock\n4.Search Stock\n5. Display Stock\n6.Exit\n")
    c=int(input("Enter Choice : "))
    if c==6:
        break
    elif c==1:
        s=input("Enter Stock to Add : ")
        if s in d.keys():
            print("Book Already Exists!")
        else:
            d[s]=int(input("Enter Stock Quantity  : "))
    elif c==2:
        s=input("Enter Stock to update : ")
        if s in d.keys():
            d[s]=input("Enter New stock quanttyt : ")
        else:
            print("Stock doesnt exist")
    elif c==3:
        s=input("Enter Stock to Del : ")
        if s in d.keys():
            del(d[s])
        else:
            print("Stock doesnt exist")
    elif c==4:
        s=input("Enter Stock to Search : ")
        if s in d.keys():
            print("Stock Quantity : ",d[s])
        else:
            print("Stock doesnt exist")
    elif c==5:
        print("Stock\tQuantity")
        for k,v in d.items():
            print(k,v)
            