class User:
 pass
#print(User)

user = User()
user.name = 'john'
user.surname = 'smit'
#print(user.name)
#print(user.surname)

class Employee:
 name = None
 age = None
 salary = None
timofey = Employee()
timofey.name = "Kuznetsow"
timofey.age = 18
timofey.salary = 1150



print(f"Данные сотрудника: имя: {timofey.name}, возраст(неточный): {timofey.age}, стипендия: {timofey.salary}. ")