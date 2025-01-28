class hello:
    def __init__(self,name):
        print("Hello",name)
        self.name = name
    def __del__(self):
        print("Goodbye",self.name)
    def callme(self):
        print("Class got called")

obj = hello("Sriram")
obj.callme()