valor_a, valor_b=input().split()
valor_a=int(valor_a)
valor_b=int(valor_b)
if valor_b!=0 and valor_a!=0:
    if valor_b%valor_a==0:
        print ("Sao Multiplos")
    elif valor_a%valor_b==0:
        print ("Sao Multiplos")
    else:
        print ("Nao sao Multiplos")