def buscar(num,lista):
    if isinstance (num,int) and isinstance (lista,list):
        return buscar1(num,lista,0)
    else: return "Error el numero no es entero o lista no es una lista"

def buscar1(num,lista,indice):
    if indice == len(lista):
        return False
    else:
        if num == lista[indice]:
            return  True
        else:
            return buscar1(num,lista,indice+1)
            
        
    
