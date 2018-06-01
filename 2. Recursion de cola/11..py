def busqueda_binaria(num,lista):
    if isinstance (num,int) and isinstance (lista,list):
        return busqueda_b(num,lista,len((lista)//2))
    else: return "Error num no es entero o la lista ingresada no es correcta"

def busqueda_b(num,lista,indice):
    print (num,lista,indice)
    if lista == []:
        return False
    elif lista[indice]== num:
        return True
    elif lista[indice]<num:
        return busqueda_b(num,lista[indice:],len((lista[indice])//2))
    else:
        return busqueda_b(num,lista[:indice],len((lista[indice])//2))
