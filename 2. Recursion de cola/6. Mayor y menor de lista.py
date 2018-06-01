def menorMayor(lista):
    if isinstance (lista,list):
        return Mayor1(lista,1,len(lista),lista[0]) , menor(lista,1,len(lista),lista[0])
    else: return "Error, no es una lista"

def Mayor1(lista,indice,largo,resultado):
    if indice == largo:
        return resultado
    elif resultado > lista[indice]:
        return Mayor1(lista,indice +1,largo,resultado)
    else: return Mayor1(lista,indice +1,largo,lista[indice])

def menor(lista,indice,largo,resultado):
    if indice == largo:
        return resultado
    elif resultado < lista[indice]:
        return menor(lista,indice +1,largo,resultado)
    else: return menor(lista,indice +1,largo,lista[indice])
    
