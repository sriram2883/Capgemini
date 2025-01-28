class parent:
    def __init__(self):
        print("This is parent class constructor")
    def func1(self):
        print("This is parent class")
class child(parent):
    def __init__(self):
        super().__init__()
        print("This is child class constructor")
    def func2(self):
        print("This is child class")
c = child()
c.func1()
c.func2()
del c