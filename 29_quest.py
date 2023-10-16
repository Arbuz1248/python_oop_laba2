class User:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def name(self, value):
        self._name = value

    def say_hello(self):
        print(f"Hello, my name is {self._name}")


class Employee(User):
    def __init__(self, name, position, department):
        super().__init__(name)
        self.position = position
        self.department = department
        self._salary = 0
        self._last_name = ""


    def salary(self):
        return self._salary


    def salary(self, value):
        self._salary = value


    def last_name(self):
        return self._last_name


    def last_name(self, value):
        self._last_name = value

    def say_hello(self):
        super().say_hello()
        print(f"I work as a {self.position} in the {self.department} department.")
        print(f"My salary is {self.salary}.")


employee = Employee("John", "Manager", "Sales")

employee.name = "Jane"
employee.last_name = "Doe"
employee.salary = 5000

employee.say_hello()