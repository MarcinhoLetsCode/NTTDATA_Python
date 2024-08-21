#import datetime
#d = datetime.date(2024, 8, 20)
#print(d)
#print(str(d.day)+"-"+str(d.month)+"-"+str(d.year))
#print(d.today())
#print(datetime.datetime.today())

from datetime import date, datetime, time
#data = datetime.date(2024, 8, 20)
data = date(2024, 8, 20)
print(data)
print(str(data.day)+"-"+str(data.month)+"-"+str(data.year))
print(date.today())

print("")
data_hora = datetime(2024, 8, 21, 10, 30, 20)
print(data_hora)
print(datetime.today())

print("")
hora = time(10, 20, 0)
print(hora)
