class User:
  __name = None

  def __init__(self,name):
    self.__name = name

  def show(self):
    self.__cape(self.__name)


  def __cape(self,stri):
    return stri
user = User('john')
print(user.show())


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
         self.__addSign(self.salary)

    def __addSign(self, num):
        return f'{num} + $'

e  = Employee('Timofey', 50)
print(e.getSalary())

