class ug:
    def __init__(self,name,rollno,marks,age):
        self.name = name
        self.__rollno = rollno
        self.marks = marks
        self.age = age
    def get_rollno(self):
        return self.__rollno
    

class pg(ug):
    def __init__(self,name,rollno,marks,age):
        super().__init__(name,rollno,marks,age)
    def display(self):
        print("Name:",self.name)
        print("Roll No:",self.get_rollno())
        print("rno: ",self._ug__rollno)
        print("Marks:",self.marks)
        print("Age:",self.age)
p = pg("Sriram",1,100,22)
p.display()