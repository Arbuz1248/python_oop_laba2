class DataManipulator:
    def __init__(self):
        self.data = {}

    def set_data(self, key, value):
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)

    def update_data(self, key, value):
        if key in self.data:
            self.data[key] = value
        else:
            print(f"Ключ '{key}' не найден в данных.")

    def delete_data(self, key):
        if key in self.data:
            del self.data[key]
        else:
            print(f"Ключ '{key}' не найден в данных.")


data_manipulator = DataManipulator()

data_manipulator.set_data("name", "John")
data_manipulator.set_data("age", 30)

print("Данные:")
print(data_manipulator.data)

# Изменение данных
data_manipulator.update_data("name", "Alice")
data_manipulator.update_data("city", "New York")

print("Обновленные данные:")
print(data_manipulator.data)

# Удаление данных
data_manipulator.delete_data("age")
data_manipulator.delete_data("country")

print("Данные после удаления:")
print(data_manipulator.data)