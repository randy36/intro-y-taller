def eliminar(num):
    if isinstance(num,int):
        return eliminar_div3(num,0,0)
    else:
        return "Error: el numero no es un entero"

def eliminar_div3(num,resultado,exponente):
    if (num == 0):
        return resultado
    elif (num %10) % 3 == 0 and (num %10) != 0:
        return eliminar_div3(num // 10, resultado, exponente)
    else: return eliminar_div3(num // 10,resultado + num % 10 *10 **exponente, exponente +1)
    
