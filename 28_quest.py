class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}")

class Employee(User):
    def __init__(self, name, position, department):
        super().__init__(name)
        self.position = position
        self.department = department


employee = Employee("Timofey", "Manager", "Sales")


employee.say_hello()