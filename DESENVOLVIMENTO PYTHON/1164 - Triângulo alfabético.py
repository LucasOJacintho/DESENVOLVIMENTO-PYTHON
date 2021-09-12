valor=int(input(''))
alfabeto=['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
contador=1
contador2=1
if valor>=1 and valor<=26:
    while contador<=valor:
        while contador2<=contador:
            print(alfabeto[contador],end="")
            contador2=contador2+1
        print(end="\n")
        contador2=1
        contador=contador+1

