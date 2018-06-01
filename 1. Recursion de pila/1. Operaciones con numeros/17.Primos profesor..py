def validar(num):
    if isinstance(num, int) and (num >1):
        return primo(num, num -1)
    else: return "Numero especial"

def primo(num,divisor):
    if divisor == 1:
        return True
    elif ((num % divisor) == 0):
        return False
    else: return primo(num, divisor -1)
