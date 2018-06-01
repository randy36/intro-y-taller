def busqueda_binaria(num,lista):
    if isinstance (num,int) and isinstance (lista,list):
        return busqueda_b(num,lista,len(lista)//2)
    else: return "Error num no es entero o la lista ingresada no es correcta"

def busqueda_b(num,lista,mitad):
    if lista == []:
        return False
    elif lista[mitad]== num:
        return True
    elif lista[mitad]<num:
        return busqueda_b(num,lista[mitad:],len((lista[mitad])//2))
    else:
        return busqueda_b(num,lista[:mitad],len((lista[mitad])//2))

 
