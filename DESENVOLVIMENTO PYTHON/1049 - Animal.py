valor_a=str(input(''))
valor_b=str(input(''))
valor_c=str(input(''))
if valor_a=='vertebrado':
    if valor_b=='ave':
        if valor_c=='carnivoro':
            print('aguia')
        elif valor_c=='onivoro':
            print('pomba')
    elif valor_b=='mamifero':
        if valor_c=='onivoro':
            print('homem')
        elif valor_c=='herbivoro':
            print('vaca')

elif valor_a=='invertebrado':
    if valor_b=='inseto':
        if valor_c=='hematofago':
            print('pulga')
        elif valor_c=='herbivoro':
            print('lagarta')
    elif valor_b=='anelideo':
        if valor_c=='hematofago':
            print('sanguessuga')
        elif valor_c=='onivoro':
            print('minhoca')
