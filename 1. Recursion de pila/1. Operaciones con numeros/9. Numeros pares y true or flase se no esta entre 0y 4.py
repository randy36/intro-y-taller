def digitos_pares(num):
    if isinstance (num, int) and num > 0:
        return digitos_pares_aux(num), Dp_entre_0y4(num)
    else:
        return "error"
def digitos_pares_aux(num):
    if num == 0:
        return 0
    elif ((num %  10) % 2 == 0):
            return 1 + digitos_pares_aux(num // 10)
    else: return digitos_pares_aux(num // 10)

def Dp_entre_0y4(num):
    if num == 0:
        return True
    elif (num % 10 >=0 and num % 10 <=4):
       return True
    else: return False
