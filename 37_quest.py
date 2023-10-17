class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(User):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_employee_info(self):
        return f"Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}"

class Programmer(Employee):
    def __init__(self, name, age, employee_id, programming_language):
        super().__init__(name, age, employee_id)
        self.programming_language = programming_language

    def get_programmer_info(self):
        return f"Programming Language: {self.programming_language}, Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}"

class Designer(Employee):
    def __init__(self, name, age, employee_id, design_tool):
        super().__init__(name, age, employee_id)
        self.design_tool = design_tool

    def get_designer_info(self):
        return f"Design Tool: {self.design_tool}, Employee ID: {self.employee_id}, Name: {self.name}, Age: {self.age}"



user = User("Timofey", 30)
print(user.get_info())

programmer = Programmer("Alice", 25, "EMP123", "Python")
print(programmer.get_programmer_info())

designer = Designer("Cirill", 28, "EMP456", "Photoshop")
print(designer.get_designer_info())