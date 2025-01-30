from items import collecteditems
from customers import customerdata
class orders:
    def list_items(self):
        items = []
        while True:
            items.append(collecteditems())
            cont = input("Do you want to add another item? (yes/no): ")
            if cont.lower() != 'yes':
                break
        return items
    def __init__(self):
        self.order_id=input("Enter order id:")
        self.date=input("Enter date:")
        self.customer=customerdata()
        self.items=self.list_items()
    def display(self):
        print("Order id:",self.order_id)
        print("Date:",self.date)
        print("Customer:")
        self.customer.display()
        print("Items:")
        for i in self.items:
            i.display()