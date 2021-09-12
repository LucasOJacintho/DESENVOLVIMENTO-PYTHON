dias=int(input(''))
anos=0
meses=0

while dias>=365:
    anos=anos+1
    dias=dias-365
while dias>=30:
    meses=meses+1
    dias=dias-30

print(anos, 'ano(s)')
print(meses, 'mes(es)')
print(dias,'dia(s)')

