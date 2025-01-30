import modules.orders as orders
# from modules.items import collecteditems
# from modules.customers import customerdata
customers_list = dict()
while(True):
    print("1.Add order\n2.Display\n3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        o=orders.orders()
        customers_list[o.customer.name]=customers_list[o.customer.name].append(o) or [o]
    elif ch==2:
        for i in customers_list:
            print(f"Customer name:{i}")
            for j in customers_list[i]:
                j.display()
    elif ch==3:
        break
    else:
        print("Invalid choice")

 