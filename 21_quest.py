class User:
	pass
user = User()
#print(isinstance(user,User))

class Student1:
  pass

class Employee1:
  pass

employee = Employee1()
print(isinstance(employee, Employee1))
print(isinstance(employee, Student1))
#True, False

class Student2:
  name = None

  def __init__(self,name):
    self.name = name

class Employee2:
  name = None

  def __init__(self,name):
    self.name = name


users = [
	 Student2('user1'),
	 Employee2('user2'),
	 Student2('user3'),
	 Employee2('user4'),
	 Student2('user5'),
	 Employee2('user6'),
	 Student2('user7'),
]
for user in users:
    if isinstance(user, Employee2):
        print(user.name)










