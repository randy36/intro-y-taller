def serie_fibonacci(num):
    if isinstance (num, int) and num > 0: 
        return serie_fibonacci_aux(num)
    else: return "Error"

def serie_fibonacci_aux(num):
    if (num == 0):
        return 1
    elif num == 1:
        return 1
    else:
        print ((num-1) + (num-2))
        return serie_fibonacci_aux(num - 1) + serie_fibonacci_aux(num - 2)

    
