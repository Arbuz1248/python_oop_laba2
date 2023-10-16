class User:
  __name = None

  def __init__(self,name,surname):
    self.__name = name

user1 = User('1', 2)
user2 = User('2', 3)


class Employee:
  __name = None

  def __init__(self, name):
    self.__name = name

#1
emp1 = Employee('john')
emp2 = Employee('eric')

print(emp1 == emp2)
#false
#2
emp3 = Employee('john')
emp4 = Employee('eric')

print(emp3 == emp3)
#true
#3
emp5 = Employee('john')
emp6 = Employee('eric')

print(emp5 != emp5)
#false
#4
emp7 = Employee('john')
emp8 = emp1

print(emp7 == emp8)
#false


#5
emp9 = Employee('john')
emp10 = Employee('eric')

print(emp9 != emp10)
#true

#6
emp11 = Employee('john')
emp12 = emp11
emp12.name = 'eric'

print(emp11 == emp12)
#true








