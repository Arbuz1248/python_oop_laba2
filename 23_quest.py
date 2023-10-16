class User:
    name = None
    position = None
    department = None

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department


class Position:
    title = None

    def __init__(self, title):
        self.title = title


class Department:
    name = None

    def __init__(self, name):
        self.name = name



position = Position("Manager")
department = Department("Sales")


user = User("John", position, department)


print("Name:", user.name)
print("Position:", user.position.title)
print("Department:", user.department.name)