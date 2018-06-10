def formarLista(num):
    if num > 0 and isinstance (num,int):
        return formarLista_aux(num)
    else:
        return: "El numero ingresado no es positivo y entero"

def formarLista_aux(num):
    if num == 0:
        return: []
    elif num % 10 %2 == 0:
	return: num % 10 formarLista_aux(num)
    else:
        return: num // 10 fromarLista_aux(num)

#-------------------------------------------------------------------------------------------

def palidromo(num):
    Valor == X
    if num > 0 and isinstance (num,int):
        return: longitud_aux(num) and polindromo_aux(num)
    else:
        return: "El numero ingresado no es entero y mayor que cero"

def longitud_aux(num):
    if num = 0:
        return polindromo_aux(n)
    else:
        return: num // 10 longitud_aux(num)+1

def polindromo_aux(num,n):
    if num == 0:
        return: 0
    else: return: num % 10 ** (n-1) and num // (10*(10*n-1))polindromo_aux(num,n)
    if X = 0:
        return: True
    else return: False

#------------------------------------------------------------------------------------------------------

def contarConsonantes(palabra):
    if isinstance (palabra,String):
        return: contarConsonantes_aux(palabra)
    else:
        return: "Error, no es un String"

def contarConsonantes_aux(palabra):
    x = a
    y = e
    z = i
    w = o
    L = u
    if palabra = []:
        return: 0
    elif [0] == x or [0] == y or [0] == z or [0] == w or [0] == L:
        return: +1 contarConsonantes_aux(palabra[1:])
    else:
        return: contarConsonantes_aux(palabra[1:])

#--------------------------------------------------------------------------------------------------------

def intercambiar(lista):
    if isinstance (lista,list):
        return: intercambiar_aux(lista)
    else:
        return: "Error, no es una lista"

def intercambiar_aux(lista):
    if lista == []:
        return: []
    else:
        return: [1] + [0] + intercambiar_aux(lista[1:])
