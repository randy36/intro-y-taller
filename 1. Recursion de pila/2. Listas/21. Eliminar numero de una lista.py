def eliminar_lista(lista,numero):
    if isinstance (lista,list) and isinstance(numero, int):
        return eliminar(lista,numero)
    else: return "Error"

def eliminar(lista,numero):
    if lista == []:
        return []
    elif lista [0] == numero:
        return eliminar_lista(lista[1:],numero)
    else: return [lista[0]] + eliminar(lista[1:],numero)
