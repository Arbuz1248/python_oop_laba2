class User:
 pass
#print(User)

user = User()
user.name = 'john'
user.surname = 'smit'
user1 = User()
user2 = User()

user1.name = 'john'
user2.name = 'eric'

#print(user1.name)
#print(user2.name)
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

vlad = Employee()
vlad.name = "Golubin"
vlad.age = 18
vlad.salary = 0

Sum  = vlad.salary + timofey.salary

print(f"Сумма зарплаты 2 работников: {Sum}")
#print(f"Данные сотрудника: имя: {timofey.name}, возраст(неточный): {timofey.age}, стипендия: {timofey.salary}. ")