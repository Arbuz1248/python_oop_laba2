class User:
    def show(self, name, surname):
        return name + ' ' + surname

class Employee:
    def smile(self,name,salary):
        return f"У сотрудника {name} заработная плата составляет: {salary}"


user = User()


employee = Employee()
employee.name = "Ilya"
employee.salary = 20000

#print(user.show('john', 'smit'))
print(employee.smile(employee.name, employee.salary))