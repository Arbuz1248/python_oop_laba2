class User:
  name = 'john'

  def show(self):
    return self.name

user = User()
print(user.name)  # 'john'
class Student:
  name = 'Ilya'
  surname = 'Maksimovich'
  def show(self):
    return self.name + ' ' + self.surname
student = Student()
print(student.show())