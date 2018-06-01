#Calcula el factorial de un numero 
def factorial (num):
      num1=abs(num)
      if num!=0:
            return num1 * factorial (num1-1)
      else:
            return 1
