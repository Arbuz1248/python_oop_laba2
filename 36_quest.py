class User:
    _name = None

    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name


class Employee(User):
    def setName(self, name):
        if len(name) > 0:
            self._name = name


user = User()
user.setName("Timofey")
print(user.getName())

employee = Employee()
employee.setName("Alice")
print(employee.getName())