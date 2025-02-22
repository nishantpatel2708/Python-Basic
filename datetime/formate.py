from datetime import datetime

dt = datetime.today()
print(dt)

dt1 = dt.strftime('%B %d %Y')
print(dt1)

dt2 = dt.strftime('%d/%b/%Y')
print(dt2)

dt3 = dt.strftime('%d-%m-%Y')
print(dt3)

dt4 = dt.strftime('%H:%M:%S')
print(dt4)

dt4 = dt.strftime('%I:%M:%S %p')
print(dt4)
print(type(dt4))

parsed_datetime = datetime.strptime(dt4, '%I:%M:%S %p')
print("Parsed datetime:", parsed_datetime)

dt_with_seconds_zero = dt.replace(second=0)

print("Original datetime:", dt)
print("Datetime with seconds set to 00:", dt_with_seconds_zero)