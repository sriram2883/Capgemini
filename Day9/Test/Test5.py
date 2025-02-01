#stock management
class stock:
    def __init__(self):
        self.name=input("Enter the name of the product:")
        self.price=float(input("Enter the price of the product:"))
        self.quantity=int(input("Enter the quantity of the product:"))
    def check(self,required):
        if self.quantity>=required:
            self.quantity-=required
            print("Product is available")
        else:
            print("Product is not available")

    def addtostock(self,required):
        self.quantity+=required
        print("Product added to stock successfully")

    def removefromstock(self,required):
        self.quantity-=required
        print("Product removed from stock successfully")
    
    def display(self):
        print(f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")
obj = stock()
obj.check(10)
obj.addtostock(5)
obj.removefromstock(2)
