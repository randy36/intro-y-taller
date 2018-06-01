def multiplica(lista):
    if isinstance (lista,list):
        return multiplicar_NDL(lista,1)
    else: return "Error, no es una lista"

def multiplicar_NDL(lista,resultado):
    if lista == []:
        return resultado
    else:
        return multiplicar_NDL(lista[1:], resultado * lista[0])
