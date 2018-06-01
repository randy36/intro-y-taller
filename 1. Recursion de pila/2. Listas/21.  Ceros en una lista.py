def ceros_lista(lista):
    if isinstance (lista,list):
        return ceros(lista)
    else: return "Error, no es una lista"

def ceros(lista):
    if lista == []:
        return False
    elif lista [0] == 0:
        return True
    else: return ceros(lista[1:])
