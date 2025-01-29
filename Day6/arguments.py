class main:
    def __init__(self,*args):
        if(len(args)==1):
            print(f"hi {args[0]}")
        elif(len(args)==2):
            print(f"hi {args[0]}, you are of {args[1]} years old")

obj=main("John")
obj=main("Jin",25)