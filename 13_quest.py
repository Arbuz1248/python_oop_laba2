class User:
  __name = None

  def __init__(self,name):
    self.__name = name

  def show(self):
    return self.__name

user = User('john')
print(user.show())


class Employee:
    __name = None
    __age =  None
    __salary = None
    def __init__(self,name,age,salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def show(self):
        return f'{self.__name}  {self.__age}  {self.__salary}'
e = Employee('Egor', 18, 2000)
print(e.show())
