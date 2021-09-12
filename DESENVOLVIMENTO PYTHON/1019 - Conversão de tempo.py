tempo=int(input(''))
horas=0
minutos=0
segundos=0

while tempo>=3600:
    horas=horas+1
    tempo=tempo-3600
while tempo>=60:
    minutos=minutos+1
    tempo=tempo-60
segundos=tempo

print(horas,':', minutos,':', segundos)