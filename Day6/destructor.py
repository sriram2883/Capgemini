class des:
    def __init__(self,name):
        self.name=name
        print(f"Hi {self.name}")
    def __del__(self):
        print(f"Bye {self.name}")
obj=des("John")
del obj

