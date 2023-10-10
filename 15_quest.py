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
user = User('john', 'smit')
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

e = Employee('Timofey', 17.1, 50)
print(e.getName())
print(e.getSalary())
print(e.getAge())




