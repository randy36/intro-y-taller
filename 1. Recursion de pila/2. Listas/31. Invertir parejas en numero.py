def invertir(num):
    if isinstance(num,int):
        return invertir_parejas(num,0)
    else: return "Error"

def invertir_parejas(num,contador):
    if num == 0 :
        return 0
    else:
        return (((num % 100) // 10) * (10 ** contador)) +((num % 10) * (10 **(contador + 1)) + invertir_parejas( num // 100,contador +2))
                                        

