class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def showName(self):
        return self.name + ' ' + self.surname
u =  User('john', 'smit')
print(u.showName())

class Employee:


    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def showName(self):
        print(self.name)
    def showSalary(self):
        print(self.salary)
    def salaryPlus(self):
        self.salary = self.salary * 1.1

employee = Employee('Timofey', 17.1, 50)
employee.showName()
employee.showSalary()
employee.salaryPlus()
employee.showSalary()
