class Employee:
    name = None
    salary = None

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employees = [
    Employee('John', 5000),
    Employee('Jane', 6000),
    Employee('Mike', 5500),
]


for employee in employees:
    print( employee.name)
    print( employee.salary)
    print()