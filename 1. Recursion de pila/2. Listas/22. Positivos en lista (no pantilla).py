def positivos_lista(lista):
    if isinstance (lista,list):
        return positivos(lista)
    else: return "Error, no es una lista"

def positivos(lista):
    if lista == []:
        return True
    elif lista [0] < 0:
        return False
    else: return positivos(lista[1:])
