import datetime

current_date = datetime.date(1901,1,1)
end_date = datetime.date(2000,12,31)

num_sundays = 0

while current_date < end_date:
  if current_date.weekday() == 6 and current_date.day == 1:
    num_sundays += 1

  current_date += datetime.timedelta(days=1)

print num_sundays