class User:
    __name = None
    __surname = None

    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    def getName(self):
        return self.__name

    def getSurn(self):
        return self.__surname

    def setName(self, name):
        self.__name = name

    def setSurn(self, surname):
        self.__surname = surname

user = User('jonh','smit')
user.setName('john')
user.setSurn('smit')

print(user.getName())
print(user.getSurn())


class Employee:
    __name = None
    __salary = None
    __age = None
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def getName(self):
        return self.__name

    def getSalary(self):
        return self.__salary

    def getAge(self):
        return self.__age

    def setName(self,name):
        self.__name = name
    def setSalary(self,salary):
        self.__salary = salary
    def setAge(self, age):
        self.__age = age

e = Employee('Timofey', 17.1, 50)
e.setName('Timofey')
e.setAge(50)
e.setSalary(17.1)


print(e.getName())
print(e.getSalary())
print(e.getAge())


