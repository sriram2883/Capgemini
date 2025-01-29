class customers:
    def __init__(self):
        self.name=input("Enter name:")
        self.phone=input("Enter phone number:")
        self.email=input("Enter email:")
        self.street=input("Enter street:")
        self.city=input("Enter city:")
        self.state=input("Enter state:")
        self.zip=input("Enter zip:")
class orders(customers):
    def __init__(self):
        super().__init__()
        self.orderid=input("Enter order id:")
        self.orderdate=input("Enter order date:")
        self.productname=input("Enter product name:")
        self.quantity=input("Enter quantity:")
        self.price=input("Enter price:")
    def display(self):
        print(f"Name:{self.name}\nPhone:{self.phone}\nEmail:{self.email}\nStreet:{self.street}\nCity:{self.city}\nState:{self.state}\nZip:{self.zip}\nOrderid:{self.orderid}\nOrderdate:{self.orderdate}\nProductname:{self.productname}\nQuantity:{self.quantity}\nPrice:{self.price}")

class orderItems(orders):
    def __init__(self):
        super().__init__()
        self.itemid=input("Enter item id:")
        self.itemname=input("Enter item name:")
        self.itemquantity=input("Enter item quantity:")
        self.itemprice=input("Enter item price:")
    def display(self):
        print(f"Name:{self.name}\nPhone:{self.phone}\nEmail:{self.email}\nStreet:{self.street}\nCity:{self.city}\nState:{self.state}\nZip:{self.zip}\nOrderid:{self.orderid}\nOrderdate:{self.orderdate}\nProductname:{self.productname}\nQuantity:{self.quantity}\nPrice:{self.price}\nItemid:{self.itemid}\nItemname:{self.itemname}\nItemquantity:{self.itemquantity}\nItemprice:{self.itemprice}")

obj=orderItems()
obj.display()