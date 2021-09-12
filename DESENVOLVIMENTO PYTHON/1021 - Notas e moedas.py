#############primeira versão

# valor=float(input(''))
# nota_100=0
# nota_50=0
# nota_20=0
# nota_10=0
# nota_5=0
# nota_2=0
# moeda_1=0
# moeda_050=0
# moeda_025=0
# moeda_010=0
# moeda_005=0
# moeda_001=0
#
# while valor>=100:
#     nota_100=nota_100+1
#     valor=valor-100
# while valor>=50:
#     nota_50=nota_50+1
#     valor=valor-50
# while valor>=20:
#     nota_20=nota_20+1
#     valor=valor-20
# while valor>=10:
#     nota_10=nota_10+1
#     valor=valor-10
# while valor>=5:
#     nota_5=nota_5+1
#     valor=valor-5
# while valor>=2:
#     nota_2=nota_2+1
#     valor=valor-2
# while valor>=1:
#     moeda_1=moeda_1+1
#     valor=valor-1
# while valor>=0.5:
#     moeda_050=moeda_050+1
#     valor=valor-0.5
# while valor>=0.25:
#     moeda_025=moeda_025+1
#     valor=valor-0.25
# while valor>=0.1:
#     moeda_010=moeda_010+1
#     valor=valor-0.1
# while valor>=0.05:
#     moeda_005=moeda_005+1
#     valor=valor-0.05
# moeda_001=valor*100
#
# print ('NOTAS:')
# print (nota_100, 'nota(s) de R$ 100,00')
# print (nota_50, 'nota(s) de R$ 50,00')
# print (nota_20, 'nota(s) de R$ 20,00')
# print (nota_10, 'nota(s) de R$ 10,00')
# print (nota_5, 'nota(s) de R$ 5,00')
# print (nota_2, 'nota(s) de R$ 2,00')
# print ('MOEDAS:')
# print (moeda_1, 'moeda(s) de R$ 1,00')
# print (moeda_050, 'moeda(s) de R$ 0,50')
# print (moeda_025, 'moeda(s) de R$ 0,25')
# print (moeda_010, 'moeda(s) de R$ 0,10')
# print (moeda_005, 'moeda(s) de R$ 0,05')
# print ("%.f" % moeda_001, 'moeda(s) de R$ 0,01')

#############segunda versão

moedas=[0,0,0,0,0,0,0,0,0,0,0,0]
valor=float(input(''))
if valor<=1000000.00:
    moedas[0]=(valor//100)
    moedas[1]=((valor-moedas[0]*100)//50)
    moedas[2]=((valor-moedas[0]*100-moedas[1]*50)//20)
    moedas[3]=((valor-moedas[0]*100-moedas[1]*50-moedas[2]*20)//10)
    moedas[4]=((valor-moedas[0]*100-moedas[1]*50-moedas[2]*20-moedas[3]*10)//5)
    moedas[5]=((valor-moedas[0]*100-moedas[1]*50-moedas[2]*20-moedas[3]*10-moedas[4]*5)//2)
    valor=(valor-moedas[0]*100-moedas[1]*50-moedas[2]*20-moedas[3]*10-moedas[4]*5-moedas[5]*2)
    print(valor)
    print ('NOTAS:')
    print ("%.f" % moedas[0], 'notas(s) de R$ 100.00')
    print ("%.f" % moedas[1], 'notas(s) de R$ 50.00')
    print ("%.f" % moedas[2], 'notas(s) de R$ 20.00')
    print ("%.f" % moedas[3], 'notas(s) de R$ 10.00')
    print ("%.f" % moedas[4], 'notas(s) de R$ 5.00')
    print ("%.f" % moedas[5], 'notas(s) de R$ 2.00')
    moedas[6]=(valor//1)
    moedas[7]=((valor-moedas[6]*1)//0.5)
    moedas[8]=((valor-moedas[6]*1-moedas[7]*0.5)//0.25)
    moedas[9]=((valor-moedas[6]*1-moedas[7]*0.5-moedas[8]*0.25)//0.10)
    moedas[10]=((valor-moedas[6]*1-moedas[7]*0.5-moedas[8]*0.25-moedas[9]*0.1)//0.05)
    moedas[11]=((valor-moedas[6]*1-moedas[7]*0.5-moedas[8]*0.25-moedas[9]*0.1-moedas[10]*0.05)/0.01)
    valor=(valor-moedas[6]*1-moedas[7]*0.5-moedas[8]*0.25-moedas[9]*0.10-moedas[10]*0.05-moedas[11]*0.01)
    print ('MOEDAS:')
    print ("%.f" % moedas[6], 'moeda(s) de R$ 1.00')
    print ("%.f" % moedas[7], 'moeda(s) de R$ 0.50')
    print ("%.f" % moedas[8], 'moeda(s) de R$ 0.25')
    print ("%.f" % moedas[9], 'moeda(s) de R$ 0.10')
    print ("%.f" % moedas[10], 'moeda(s) de R$ 0.05')
    print ("%.f" % moedas[11], 'moeda(s) de R$ 0.01')
    print(valor)