class Employee:
    name = None
    salary = None

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeesCollection:
    employees = []

    def addEmployee(self, employee):
        self.employees.append(employee)

    def printEmployees(self):
        for employee in self.employees:
            print(employee.name)
            print( employee.salary)
            print()

    def getTotalSalary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary

    def getAverageSalary(self):
        if len(self.employees) > 0:
            total_salary = self.getTotalSalary()
            average_salary = total_salary / len(self.employees)
            return average_salary
        else:
            return 0



collection = EmployeesCollection()


collection.addEmployee(Employee('Timofey', 5000))
collection.addEmployee(Employee('Illya', 6000))
collection.addEmployee(Employee('Vlad', 5500))


collection.printEmployees()


total_salary = collection.getTotalSalary()
print( total_salary)


average_salary = collection.getAverageSalary()
print( average_salary)