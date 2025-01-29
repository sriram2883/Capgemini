class cat:
    def sound(self):
        print("Meow")

class dog:
    def sound(self):
        print("Bark")

for animal in ([cat(), dog()]):
    animal.sound()
