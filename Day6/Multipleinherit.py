class man:
    def man(self):
        print("I am man")
class women:
    def women(self):
        print("I am women")
class person(women,man):
    pass

obj=person()
obj.man()
obj.women()