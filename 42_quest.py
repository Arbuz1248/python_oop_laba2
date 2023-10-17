from datetime import datetime

class Zate:
    def __init__(self, year, month, day):
        self.date = datetime(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def get_weekday_number(self):
        return self.date.weekday()

    def get_weekday_name(self):
        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        return weekdays[self.get_weekday_number()]

    def get_month_name(self):
        months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        return months[self.get_month() - 1]


date = Zate(2023, 10, 17)

print("Год:", date.get_year())
print("Месяц:", date.get_month())
print("День:", date.get_day())
print("Номер дня недели (0 - Пн, 6 - Вс):", date.get_weekday_number())
print("День недели:", date.get_weekday_name())
print("Месяц:", date.get_month_name())