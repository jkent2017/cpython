import datetime
day = datetime.date(2020,3,2)
dayNum = day.weekday()
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

dayString = weekDays[dayNum]
print(f'\nDate with an C.E. year: {dayString}\n')

day = datetime.date(-380,3,2)
dayNum = day.weekday()

dayString = weekdays[dayNum]
print(f'Date with an B.C.E. year: {dayString}')
