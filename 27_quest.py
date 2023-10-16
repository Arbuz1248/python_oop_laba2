
class User:
    def __init__(self, name):
        self.name = name

class Employee(User):
    def __init__(self, name, position, department):
        super().__init__(name)
        self.position = position
        self.department = department

employee = Employee("Timofey", "Manager", "Sales")

print(employee.name)
print(employee.position)
print(employee.department)