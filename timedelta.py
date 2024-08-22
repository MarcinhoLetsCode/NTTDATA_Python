import datetime
d = datetime.date(2024, 8, 20)
print(d)
print(str(d.day)+"-"+str(d.month)+"-"+str(d.year))

print("")
d = d + datetime.timedelta(weeks=1)
print(d)
print(str(d.day)+"-"+str(d.month)+"-"+str(d.year))

from datetime import datetime, timedelta, date, time

tipo_carro = 'P' # P M G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
#data_atual = datetime.today()
data_atual = datetime.now()
#data_atual = datetime.utcnow()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes = tempo_pequeno)
    print(f'O carro chegou: {data_atual.hour} e ficará pronto as: {data_estimada}')
    #pass
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes = tempo_medio)
    print(f'O carro chegou: {data_atual} e ficará pronto as: {data_estimada}')
    #pass
else:
    data_estimada = data_atual + timedelta(minutes = tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará pronto as: {data_estimada}')
    #pass
    
#print(data_estimada)
    
print('')
#data = date(2024, 8, 22)
data = date.today()
print(data - timedelta(days=1))

resultado = datetime(2024, 8, 22, 17, 00, 00) - timedelta(hours=1)
print(resultado.time())
