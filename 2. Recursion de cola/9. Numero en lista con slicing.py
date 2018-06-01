def buscar(num,lista):
    if isinstance(num,int) and isinstance (lista,list):
        return buscar1(num,lista)
    else: return "Error"

def buscar1(num,lista):
    if lista == []:
        return False
    else:
        if num == lista[0]:
            return  True
        else:
            return buscar1(num,lista[1:])
