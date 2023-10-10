class User:
  name = None
  def show(self):
    print(self.name)



user = User()
user.name = 'john'
user.show()

class Employee:
    name = None
    salary = None
    def showName(self):
        print(self.name)
    def showSalary(self):
        print(self.salary)

employee = Employee()

employee.name = 'Max'
employee.salary = 11000
employee.showName()
employee.showSalary()

