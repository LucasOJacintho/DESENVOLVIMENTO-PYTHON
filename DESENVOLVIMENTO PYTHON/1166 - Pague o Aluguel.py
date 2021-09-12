divida=int(input(''))
valor_mensal=int(input(''))
pagamento=0

while divida>0:
    pagamento=pagamento+1
    print('pagamento:', pagamento)
    print('antes =', divida)
    divida=divida-valor_mensal
    if divida>=0:
        print('depois =', divida)
    else:
        print('depois = 0')
    print('-----')
