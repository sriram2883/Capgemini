class collecteditems:
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

