class User:
    __name = None
    __surname = None

    def getName(self):
        return self.__name

    def getSurn(self):
        return self.__surname

    def setName(self, name):
        if (len(name) > 0):
            self.__name = name
        else:
            raise Exception('name is incorrect')

    def setSurn(self, surname):
        if (len(surname) > 0):
            self.__surname = surname
        else:
            raise Exception("surname is incorrect!")

user = User()
user.setName('john')

class Employee:
    __name = None
    __salary = None
    __age = None


    def setAge(self, age):
        if (age > 0 and age < 120):
            self.__age = age
            return f"{age}"
        else:
            return f"number {age} is not correct"

    def getSalary(self):
        return f"{self.__salary} $"

e = Employee()
print(e.setAge(125))
print(e.setAge(67))
print(e.getSalary())


#В классе Employee в сеттере возраста сделайте проверку на то, что возраст должен быть от 0 до 120.
#В классе Employee в геттере зарплаты сделайте так, чтобы при чтении зарплаты в конец ее значения добавлялся знак доллара.