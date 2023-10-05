class Car:
    color = None  # цвет автомобиля
    fuel = None  # количество топлива
    max_speed = None # максимальныая скорость
    seats = None # кол-во мест
    def go(self):
        # Команда ехать:
        pass

    def turn(self):
        # Команда поворачивать:
        pass
    def info(self):

        return(f"Информация о машине:  цвет:  {myCar.color}, Количество топлива:  {myCar.fuel}, "
                    f"Мест:  {myCar.seats}, Макс. скорость: {myCar.max_speed}")
    def stop(self):
        # Команда остановиться:
        pass

class Jeap(Car):
    def a(self):
        jeap = Jeap()
        jeap.color = 'Blue'
        jeap.fuel = 120
        jeap.max_speed = 200
        jeap.seats = 5
        return (f"Информация о машине:  цвет:  {jeap.color}, Количество топлива:  {jeap.fuel}, "
                f"Мест:  {jeap.seats}, Макс. скорость: {jeap.max_speed}")

myCar = Jeap()
myCar.color = 'red'  # красим в красный цвет
myCar.fuel = 50    # заливаем топливо
myCar.max_speed = 90 # указываем скорость
myCar.seats = 4 # указываем кол-во мест
myCar.go()
myCar.turn()
myCar.stop()
print(myCar.a())