def invertir(lista):
    if isinstance (lista,list):
        return invertir_lista(lista)
    else: return "Error, la lista ingresada no es valida"

def invertir_lista(lista):
    if lista == []:
        return []
    else: return [lista[-1]] + invertir_lista(lista [:-1])
