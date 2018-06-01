def operacion(num):
    if isinstance (num, int) and num > 0: 
        return operacion_aux(num)
    else: return "Error"

def operacion_aux(num):
    if (num == 0):
        return 1
    else:
        return (3 * num -2) * operacion_aux(num-1)
