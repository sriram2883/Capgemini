class main:
    def __init__(self,sname,**args):
        self.sname=sname
        if(len(args)==1):
            print(f"hi {args['name']}")
        elif(len(args)==2):
            print(f"hi {args['name']}, you are of {args['age']} years old")

obj=main(name="John",sname="Doe")
obj=main(name="Jin",age=25,sname="Doe")
print(obj.sname)