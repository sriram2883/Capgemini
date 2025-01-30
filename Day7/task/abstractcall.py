from abc import ABC, abstractmethod
class Father(ABC):
    @abstractmethod
    def profession(self):
        pass
    def intro(self):
        self.profession()
class Engineer(Father):
    def profession(self):
        print("I am an Engineer")
class Doctor(Father):
    def profession(self):
        print("I am a Doctor")
    
e=Engineer()
e.intro()
d=Doctor()
d.intro()