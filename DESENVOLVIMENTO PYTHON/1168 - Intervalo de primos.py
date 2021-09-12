inicio=int(input(''))
fim=int(input(''))
divisor=1
verificador=0
contador=0
if inicio<=fim<=5000:
    while inicio<=fim:
        while (inicio-1)>divisor and verificador!=1:
            divisor = divisor + 1
            if inicio%divisor==0:
                verificador=1
        if verificador==0 and inicio>1:
            print(inicio)
            contador=contador+1
        inicio = inicio + 1
        divisor = 1
        verificador = 0
    print("primos:", contador)