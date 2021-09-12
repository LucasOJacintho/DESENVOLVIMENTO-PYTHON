ano1=int(input(''))
ano2=int(input(''))
contador=0
if ano1>=0 and ano2<=9999:
    while ano1<=ano2:
        if ano1%4==0 and ano1%100!=0 or ano1%400==0:
            print(ano1)
            contador=contador+1
        ano1=ano1+1
    print("bissextos:", contador)