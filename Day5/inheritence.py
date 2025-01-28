class parent:
    def display_parent(self):
        print("This is parent method")
class child(parent):
    def display_child(self):
        print("This is child method")

c = child()
c.display_parent()
c.display_child()
del c