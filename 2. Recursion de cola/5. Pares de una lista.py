def lista2(lista):
    if isinstance(lista,list) and lista != []:
        return lista2_aux(lista,0,len(lista),[])
    else:
        return "Error"

def lista2_aux(lista,indice,largo,resultado):
    if indice == largo:
        return resultado
    elif lista[indice]%2 == 0:
        return (lista2_aux(lista,indice + 1, largo, [lista[indice]] +resultado))
    else: return (lista2_aux(lista,indice + 1, largo,resultado))

