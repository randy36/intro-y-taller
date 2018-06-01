def primos_lista(lista):
    if isinstance (lista,list):
        return recorrer_lista(lista)
    else: return "Error, la lista ingresada no es valida"

def recorrer_lista(lista):
    if lista == []:
        return []
    elif primos(lista[0], lista[0] -1) == True:
        return [lista[0]] + recorrer_lista(lista[1:])
    else: return recorrer_lista(lista[1:])

def primos(numero,contador):
    if numero == 0 or numero == 1 or numero == 2 or numero == 3:
        return True
    elif contador == 1:
        return True
    elif numero % contador == 0:
        return False
    else: return primos(numero,contador -1)
