class customers:
    def __init__(self):
        self.name=input("Enter name:")
        self.phone=input("Enter phone number:")
        self.email=input("Enter email:")
        self.street=input("Enter street:")
        self.city=input("Enter city:")
        self.state=input("Enter state:")
        self.zip=input("Enter zip:")
    def display(self):
        print("Name:",self.name)
        print("Phone:",self.phone)
        print("Email:",self.email)
        print("Street:",self.street)
        print("City:",self.city)
        print("State:",self.state)
        print("Zip:",self.zip)
class orders:
    def list_items(self):
        items = []
        while True:
            items.append(Items())
            cont = input("Do you want to add another item? (yes/no): ")
            if cont.lower() != 'yes':
                break
        return items
    def __init__(self):
        self.order_id=input("Enter order id:")
        self.date=input("Enter date:")
        self.customer=customers()
        self.items=self.list_items()
    def display(self):
        print("Order id:",self.order_id)
        print("Date:",self.date)
        print("Customer:")
        self.customer.display()
        print("Items:")
        for i in self.items:
            i.display()
class Items:
    def __init__(self):
        self.item_id=input("Enter item id:")
        self.name=input("Enter name:")
        self.price=input("Enter price:")
        self.quantity=input("Enter quantity:")
    def display(self):
        print("Item id:",self.item_id)
        print("Name:",self.name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
customers_list = dict()
while(True):
    print("1.Add order\n2.Display\n3.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        o=orders()
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