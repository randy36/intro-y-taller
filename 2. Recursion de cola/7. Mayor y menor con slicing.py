def mayorMenor(lista):
    if isinstance (lista,list) and lista != []:
        return mayor_aux(lista,lista[0]), menor_aux(lista, lista[0])
    else: return "Error"

def mayor_aux(lista,mayor):
    if lista == []:
        return mayor
    elif lista [0] > mayor:
        return mayor_aux(lista [1:], lista[0])
    else:
        return mayor_aux(lista[1:],mayor)

def menor_aux(lista,menor):
    if lista == []:
        return menor
    elif lista [0] < menor:
        return menor_aux(lista [1:], lista[0])
    else:
        return menor_aux(lista[1:],menor)
