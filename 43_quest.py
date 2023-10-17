from datetime import timedelta
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


class ZateExt(Zate):
    def add_years(self, years):
        new_date = self.date + timedelta(days=365 * years)
        return Zate(new_date.year, new_date.month, new_date.day)

    def subtract_years(self, years):
        new_date = self.date - timedelta(days=365 * years)
        return Zate(new_date.year, new_date.month, new_date.day)

    def add_months(self, months):
        new_date = self.date.replace(day=1, month=self.date.month + months)
        while new_date.month != ((self.date.month + months) % 12):
            new_date -= timedelta(days=1)
        return Zate(new_date.year, new_date.month, new_date.day)

    def subtract_months(self, months):
        new_date = self.date.replace(day=1, month=self.date.month - months)
        while new_date.month != ((self.date.month - months) % 12):
            new_date -= timedelta(days=1)
        return Zate(new_date.year, new_date.month, new_date.day)

    def add_days(self, days):
        new_date = self.date + timedelta(days=days)
        return Zate(new_date.year, new_date.month, new_date.day)

    def subtract_days(self, days):
        new_date = self.date - timedelta(days=days)
        return Zate(new_date.year, new_date.month, new_date.day)

# Пример использования:
date = ZateExt(2023, 10, 17)

# Прибавление и вычитание лет
new_date_plus_3_years = date.add_years(3)
new_date_minus_2_years = date.subtract_years(2)

# Прибавление и вычитание месяцев
new_date_plus_6_months = date.add_months(6)
new_date_minus_4_months = date.subtract_months(4)

# Прибавление и вычитание дней
new_date_plus_10_days = date.add_days(10)
new_date_minus_5_days = date.subtract_days(5)