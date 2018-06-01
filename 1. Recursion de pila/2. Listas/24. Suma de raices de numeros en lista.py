def suma(lista):
    if isinstance (lista,list):
        return suma_raices(lista)
    else: return "Error, no es una lista"

def suma_raices(lista):
    if lista == []:
        return 0
    else:
        import math
        return (math.sqrt(lista[0])+suma_raices(lista[1:]))
