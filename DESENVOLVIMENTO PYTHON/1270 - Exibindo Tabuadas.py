valor_1=int(input(''))
valor_2=int(input(''))
contador=1
if valor_1>valor_2:
    print('Nenhuma tabuada no intervalo!')

while valor_1<=valor_2:
    while contador<=10:
        print(valor_1,'x',contador,'=',valor_1*contador)
        contador+=1
    print('----------')
    contador=1
    valor_1+=1