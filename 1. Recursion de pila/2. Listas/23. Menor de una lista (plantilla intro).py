def menor_lista(lista):
    if isinstance (lista,list):
        return menor(lista)
    else: return "Error, no es una lista"

def menor(lista):
    if len(lista) == 1:
        return lista[0]
    if lista [0] <= lista [1]:
        return menor([lista[0]]+lista[2:])
    elif lista [0] >= lista [1]:
        return menor(lista[1:])
