from datetime import datetime

class Period:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def seconds_difference(self):
        delta = self.end_time - self.start_time
        return delta.total_seconds()

    def minutes_difference(self):
        return self.seconds_difference() / 60

    def hours_difference(self):
        return self.minutes_difference() / 60

    def days_difference(self):
        return self.hours_difference() / 24

start_time = datetime(2023, 10, 17, 12, 0, 0)
end_time = datetime(2023, 10, 18, 12, 0, 0)

period = Period(start_time, end_time)

print("Разница в секундах:", period.seconds_difference())
print("Разница в минутах:", period.minutes_difference())
print("Разница в часах:", period.hours_difference())
print("Разница в днях:", period.days_difference())