def suma(lista):
    if isinstance(lista,list):
        return suma_potencia(lista,0)
    else:
        return "Lo ingresado no es una lista"

def suma_potencia(lista,n):
    if lista == []:
        return 0
    elif isinstance(lista[0],list):
            #return suma_potencia(lista[0],n) + suma_potencia(lista[1:],n+len(lista[0]))
            return suma_potencia(lista[0]+lista[1:],n)
    else: return (lista[0]**(n+1)) + suma_potencia(lista[1:],n+1)
