import datetime

d = datetime.date(2024, 8, 20)
print(d)
print(str(d.day)+"-"+str(d.month)+"-"+str(d.year))

print("")
d = d + datetime.timedelta(weeks=1)
print(d)
print(str(d.day)+"-"+str(d.month)+"-"+str(d.year))

from datetime import datetime

d = datetime.now()

#FORMATANDO DATA E HORA
print(d.strftime("%d/%m/%Y %a %H:%M:%S"))

#CONVERTENDO STRING PARA DATETIME
date_string = "22/08/2024 17:00"
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d) #2024-08-22 17:00
