file = open('test_pr2.txt', 'r')
texto = file.read()
parrafos = texto.split('\n\n')
parrafos_leidos = 0
for i in parrafos:
    en_veces = 0
    En_veces = 0
    palabras = i.split(' ')
    for e in palabras:
        if (e == 'en'):
            en_veces += 1
        if (e == 'En'):
            En_veces += 1
    parrafos_leidos += 1        
    print(f"En el parrafo {parrafos_leidos} la palabra 'en' esta repetida {en_veces} veces")
    if En_veces>0:
        print(f"En el parrafo {parrafos_leidos} la palabra 'En' esta repetida {En_veces} veces")