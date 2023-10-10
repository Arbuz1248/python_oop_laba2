class User:

    def __init__(self, name, surname):
        print(name + ' ' + surname)
u =  User('john', 'smit')


class Employee:
    name = None
    age = None
    salary = None

    def __init__(self, name, salary):
        print(f'{name} {salary}')
employee = Employee('Timofey', 50)
