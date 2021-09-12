canais=int(input(''))
canaisma1=canais
pos=0
canal = []
cont=0
if canais>=1 and canais<=200:
    while canais>0:
        canal.append(input().split(';'))
        canal[pos][1] = int(canal[pos][1])
        canal[pos][2] = float(canal[pos][2])
        # print(canal)
        canais-=1
        pos+=1
    pos=0
    valorcp=float(input(''))
    valorsp=float(input(''))
    print('-----')
    print('BÔNUS')
    print('-----')

    while canaisma1>0:
        if canal[pos][3]=='sim':
            while canal[pos][1]>=1000:
                canal[pos][1]=canal[pos][1]-1000
                cont += 1
            print(canal[pos][0], end="")
            print(": R$","%.2f"%((cont*valorcp)+canal[pos][2]))
            cont=0
        else:
            while canal[pos][1]>=1000:
                canal[pos][1]=canal[pos][1]-1000
                cont += 1
            print(canal[pos][0], end="")
            print(": R$", "%.2f" % ((cont * valorsp) + canal[pos][2]))
            cont=0

        canaisma1-=1
        pos += 1
