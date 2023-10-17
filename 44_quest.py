import calendar

class Month:
    def __init__(self, month_number):
        self.month_number = month_number

    def get_month_number(self):
        return self.month_number

    def get_month_name(self):
        month_names = [
            "Январь", "Февраль", "Март", "Апрель",
            "Май", "Июнь", "Июль", "Август",
            "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
        ]
        return month_names[self.month_number - 1]

    def get_last_day_number(self):
        _, last_day = calendar.monthrange(2023, self.month_number)
        return last_day

    def get_first_weekday(self):
        first_day = 1
        _, first_weekday = calendar.monthrange(2023, self.month_number)
        return first_weekday

    def get_last_weekday(self):
        last_day = self.get_last_day_number()
        _, last_weekday = calendar.monthrange(2023, self.month_number, last_day)
        return last_weekday


month = Month(10)

print("Номер месяца:", month.get_month_number())
print("Название месяца:", month.get_month_name())
print("Номер последнего дня месяца:", month.get_last_day_number())
print("Номер дня недели первого дня месяца:", month.get_first_weekday())
print("Номер дня недели последнего дня месяца:", month.get_last_weekday())