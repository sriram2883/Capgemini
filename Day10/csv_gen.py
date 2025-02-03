class Employee:
    def __init__(self,name,id,department):
        self.name = name
        self.id = id
        self.department = department
        self.log()
    def log(self):
        log_file = open("Day10/log.csv","a+")
        arr = [str(self.id),self.name,self.department]
        log_file.write(",".join(arr) + "\n")
        print(f"Employee with id {self.id} is logged")
        log_file.close()

print("Create emp objects")
while True:
    name = input("Enter the name of Employee: ")
    id = int(input("Enter the id of Employee: "))
    department = input("Enter the department of Employee: ")
    obj = Employee(name,id,department)
    print("Enter no to exit creation")
    opt = input()
    if(opt == "no"):
        break
    