d={}
while True:
    print("1. Update Stock\n2. Add Stock\n3. Delete Stock\n4. Search Stock\n5. Display Stocks\n6. Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        print("Update Stock")
        bn=input("Enter Book Name : ")
        if bn in list(d.keys()):
            print(bn,"Exists")
        else:
            print(bn,"Doesnt Exist yet")
            d[bn]=int(input("Enter Stock Quantity : "))
    elif ch==2:
        print("Add Stock")
        bn=input("Enter Book Name : ")
        if bn in list(d.keys()):
            print(bn,"Exists")
            addn=int(input("Enter Nuber of stocks yo be added : "))
            d[bn]+=addn 
        else:
            print(bn,"Doesnt Exist ")
    elif ch==3:
        print("Delete Stock")
        bn=input("Enter Book Name to be deleted : ")
        if bn in list(d.keys()):
            del d[bn]
            print(bn,"Deleted") 
        else:
            print(bn,"Doesnt Exist ")
    elif ch==4:
        print("Search Stock")
        bn=input("Enter Book Name to be Searched : ")
        if bn in list(d.keys()):
            print("BookName : ",bn,"\nStocks : ",d[bn]) 
        else:
            print(bn,"Doesnt Exist ")
    elif ch==5:
    		print("BookName  Stock")
    		for i in list(d.keys()):
    			print(i,d[i])
    
    elif ch==6:
        break
