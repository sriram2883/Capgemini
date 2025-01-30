from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(animal):
    def make_sound(self):
        print("Bark")
class cat(animal):
    def make_sound(self):
        print("Meow")

d=dog()
c=cat()
d.make_sound()
c.make_sound()