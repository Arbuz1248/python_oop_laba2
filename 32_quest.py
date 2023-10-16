class User:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Мое имя {self.name}")


class Employee(User):
    def __init__(self, name, age, salary):
        super().__init__(name)
        self._age = age
        self._salary = salary

    def age(self):
        return self._age

    def salary(self):
        return self._salary


employee = Employee("Timofey", 30, 5000)

print(employee.age)
print(employee.salary)