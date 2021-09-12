alunos=int(input(''))
alunos_ma1=alunos
alunos_ma2=alunos
notasalteradas=0
posa=0
nota=[]
cont=1
if alunos>=1 and alunos<=999:
    while alunos>0:
        nota.append(input().split())
        nota[posa][0]=float(nota[posa][0])
        alunos=alunos-1
        posa+=1
    posa=0

    while alunos_ma1>0:
        nota[posa].append(input())
        nota[posa][1] = float(nota[posa][1])
        if nota[posa][1]==10:
            nota[posa].append(2)
            nota[posa].append('*')
            nota[posa].append(nota[posa][0]+2)
            notasalteradas += 1
            if nota[posa][0]==10 and nota[posa][1]==10:
                notasalteradas-=1
                nota[posa][3]='-'
            if nota[posa][4]>10:
                nota[posa][4]=10
        else:
            nota[posa].append(0)
            nota[posa].append('-')
            nota[posa].append(nota[posa][0])
        alunos_ma1= alunos_ma1 - 1
        posa+=1
    posa=0
    print('NOTAS ALTERADAS:',notasalteradas)
    while alunos_ma2>0:
        print(nota[posa][3],end ="")
        print('('f"{cont:03}"') original:',"{0:05.2f}".format(nota[posa][0]), "| final:", "{0:05.2f}".format(nota[posa][4]))
        alunos_ma2-=1
        cont+=1
        posa+=1