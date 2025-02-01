#multiple inheritance
class Areoplane:
    def move(self):
        print("Areoplane can fly")

class car:
    def move(self):
        print("Car can move on road")


class Hybrid(car, Areoplane):
    def move(self):
        print("Hybrid can move on road and fly")

obj = Hybrid()
obj.move()
