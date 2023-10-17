class User:
    def __init__(self):
        self.__name = ''

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

class Employee(User):
    user = User()
    user.setName("Timofey")
    print(user.getName())

employee = Employee()
employee.setName("Alice")
print(employee.getName())