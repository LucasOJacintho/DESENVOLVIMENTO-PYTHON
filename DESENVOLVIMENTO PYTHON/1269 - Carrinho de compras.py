valor=[]
valor.append(input().split())
comp=len(valor[0])
item=0
achar=0
lista=1
while item < comp:
    valor[0][item] = int(valor[0][item])
    item += 1
item=0
valor.append(input().split())

while valor[lista][0]!='encerrar':
    comp=len(valor[0])

    if valor[lista][0]=='exibir':
        item=0
        valor[0].sort()
        while item<comp-1:
            print(valor[0][item],end =" ")
            item+=1
        print(valor[0][item])

    elif valor[lista][0]=='adicionar':
        valor[lista][1] = int(valor[lista][1])
        valor[0].append(valor[lista][1])

    elif valor[lista][0]=='remover':
        item=0
        valor[lista][1] = int(valor [lista][1])
        while achar==0:
            if item==comp:
                print('código', valor[lista][1], 'não encontrado')
                achar = 1
            elif valor[0][item]==valor[lista][1]:
                del valor[0][item]
                achar=1
            item+=1

    valor.append(input().split())
    comp = len(valor[0])
    lista+=1
    achar=0
    item=0

valor[0].sort()
while item<comp-1:
    print(valor[0][item], end=" ")
    item+=1
print(valor[0][item])