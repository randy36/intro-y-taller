def aparece(num, digito):
    if ((isinstance (num, int) and isinstance (digito, int) and digito >=0 and digito <= 9) and (num > 0)):
        return aparece_aux(num, digito)
    else:
        return "error"
def aparece_aux(num, digito):
    if num == 0:
        return 0
    else:
        if num % 10 == digito:
            return 1 + aparece_aux(num // 10,digito)
        else: return aparece_aux(num // 10, digito)








                                    
