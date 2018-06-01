def sumas_pares_impares(lista):
    if isinstance (lista, list):
        return pares_aux(lista)
    else: return "Error"

def pares_aux(lista):
    if lista == []: #luz roja
        return 0
    elif lista[0] % 2 == 0: #luz verde
        return lista[0] + pares_aux(lista[1:]) # par
    else: return pares_aux(lista[1:]) #impar
    
