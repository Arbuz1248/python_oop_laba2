class User:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name

    def name(self, value):
        self._name = value

    def say_hello(self):
        print(f"Привет, мое имя {self._name}")

class Employee(User):
    def __init__(self, name, position, department):
        super().__init__(name)
        self.position = position
        self.department = department
        self._salary = 0
        self._age = 0


    def salary(self):
        return self._salary


    def salary(self, value):
        self._salary = value


    def age(self):
        return self._age


    def age(self, value):
        if 18 <= value <= 65:
            self._age = value
        else:
            raise ValueError("Возраст должен быть между 18 и 65")

    def say_hello(self):
        super().say_hello()
        print(f"Я работаю {self.position} в {self.department} департаменте.")
        print(f"Моя зарплата {self.salary}.")
        print(f"Мне {self.age} лет.")


employee = Employee("Timofey", "Manager", "Sales")


employee.age = 30


employee.say_hello()


try:
    employee.age = 17
except ValueError as e:
    print(str(e))