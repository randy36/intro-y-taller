def digitos_pares_impares(num):
    if isinstance (num, int) and num > 0:
        return digitos_pares(num), impares(num)
    else:
        return "error"
def digitos_pares(num):
    if num == 0:
        return 0
    elif ((num %  10) % 2 == 0):
            return 1 + digitos_pares(num // 10)
    else: return digitos_pares(num // 10)

def impares(num):
    if num == 0:
        return 0
    elif ((num % 10) % 2) == 1:
            return 1 + impares(num // 10)
    else:
        return impares (num // 10)
