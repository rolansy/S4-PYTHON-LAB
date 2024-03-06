d = {}

while True:
    print("1. Add Stock")
    print("2. Update Stock")
    print("3. Delete Stock")
    print("4. Search Stock")
    print("5. Display Stocks")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        print("\nAdd Stock")
        bn = input("Enter Book Name: ")

        if bn in list(d.keys()):
            print(bn, "Exists")
        else:
            d[bn] = int(input("Enter Stock Quantity: "))

    elif ch == 2:
        print("\nUpdate Stock")
        bn = input("Enter Book Name: ")

        if bn in list(d.keys()):
            print(bn, "Exists")
            addn = int(input("Enter Number of stocks to be added: "))
            d[bn] += addn
        else:
            print(bn, "Doesn't Exist")

    elif ch == 3:
        print("\nDelete Stock")
        bn = input("Enter Book Name to be deleted: ")

        if bn in list(d.keys()):
            del d[bn]
            print(bn, "Deleted")
        else:
            print(bn, "Doesn't Exist")

    elif ch == 4:
        print("\nSearch Stock")
        bn = input("Enter Book Name to be Searched: ")

        if bn in list(d.keys()):
            print("Book Name:", bn)
            print("Stocks:", d[bn])
        else:
            print(bn, "Doesn't Exist")

    elif ch == 5:
        print("\nDisplay Stocks")
        print(f"{'Book Name':<10}{'Stock':7}")
        for i in list(d.keys()):
            print(f"{i:<8}{d[i]:^7}")

    elif ch == 6:
        break
        
