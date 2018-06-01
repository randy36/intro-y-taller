def elevado(num):
    if isinstance (num, int) and num > 0: 
        return elevado_aux(num)
    else: return "Error"

def elevado_aux(num):
    if (num == 0):
        return 0
    else:
        return num *num **3 + elevado_aux(num-1)
