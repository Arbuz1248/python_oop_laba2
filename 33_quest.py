class User:
    def __init__(self):
        self.__name = None
        self.__surname = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSurn(self, surname):
        self.__surname = surname

    def getSurn(self):
        return self.__surname

class Employee(User):
    def getFull(self):
        return self.getName() + ' ' + self.getSurn()


employee = Employee()


employee.setName("Timofey")
employee.setSurn("Kuznetsov")


print(employee.getName())
print(employee.getSurn())


print( employee.getFull())