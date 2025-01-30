class customerdata:
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