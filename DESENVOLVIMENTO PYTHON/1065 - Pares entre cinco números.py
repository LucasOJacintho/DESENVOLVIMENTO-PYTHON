valor_a=int(input(''))
valor_b=int(input(''))
valor_c=int(input(''))
valor_d=int(input(''))
valor_e=int(input(''))
pares=0
if valor_a%2==0:
    pares+=1
if valor_b%2==0:
    pares+=1
if valor_c%2==0:
    pares+=1
if valor_d%2==0:
    pares+=1
if valor_e%2==0:
    pares+=1

print(pares,"valores pares")