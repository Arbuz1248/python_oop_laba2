class User:
  name = 'oop python'

  def show(self):
    return self.cape(self.name)

  def cape(self,stri):
    return stri.upper()

user = User()
user.name = 'Papa Jonse'
print(user.show())

class Student:
  name = None
  surname = None



  def show(self):
    return self.inital(self.name,self.surname)

  def inital(self,dad1,dad2):
    return dad1[0].upper() + '. ' + dad2[0].upper() + '.'

student = Student()
student.name = 'Alex'
student.surname = 'March'
print(student.inital(student.name, student.surname))