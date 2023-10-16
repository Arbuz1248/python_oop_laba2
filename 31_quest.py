class User:
    def setAge(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception('Нужен возраст больше 0')


class Employee(User):
    def setAge(self, age):
        try:
            super().setAge(age)
            if age > 120:
                raise Exception('Нужен возраст меньше 120')
        except Exception as e:
            raise e


employee = Employee()
employee.setAge(30)
print(employee.age)

try:
    employee.setAge(-5)
except Exception as e:
    print(str(e))

try:
    employee.setAge(150)
except Exception as e:
    print(str(e))