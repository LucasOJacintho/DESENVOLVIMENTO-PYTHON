valor=int(input(''))
nota_100=0
nota_50=0
nota_20=0
nota_10=0
nota_5=0
nota_2=0
nota_1=0
while valor>=100:
    nota_100=nota_100+1
    valor=valor-100
while valor>=50:
    nota_50=nota_50+1
    valor=valor-50
while valor>=20:
    nota_20=nota_20+1
    valor=valor-20
while valor>=10:
    nota_10=nota_10+1
    valor=valor-10
while valor>=5:
    nota_5=nota_5+1
    valor=valor-5
while valor>=2:
    nota_2=nota_2+1
    valor=valor-2
while valor==1:
    nota_1=nota_1+1
    valor=valor-1
print(valor)
print(nota_100, 'nota(s) de R$ 100,00')
print(nota_50, 'nota(s) de R$ 50,00')
print(nota_20, 'nota(s) de R$ 20,00')
print(nota_10, 'nota(s) de R$ 10,00')
print(nota_5, 'nota(s) de R$ 5,00')
print(nota_2, 'nota(s) de R$ 2,00')
print(nota_1, 'nota(s)de R$1,00')