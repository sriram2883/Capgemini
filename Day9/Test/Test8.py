#animal

class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def speak(self):
        print("Dog Barking")

class Cat(Animal):
    def speak(self):
        print("Cat Meowing")

dog = Dog()
dog.speak()
cat = Cat()
cat.speak()