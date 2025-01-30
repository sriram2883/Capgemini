from abc import ABC, abstractmethod
class parent:
    @abstractmethod 
    def setpannum(self):
        pass
class son(parent):
    def setpannum(self):
        self.pannum=input("Enter pan number:")
    def display(self):
        print("Pan number:",self.pannum)
class daughter(parent):
    def setpannum(self):
        self.pannum=input("Enter pan number:")
    def display(self):
        print("Pan number:",self.pannum)
s=son()
d=daughter()
s.display()
d.display()