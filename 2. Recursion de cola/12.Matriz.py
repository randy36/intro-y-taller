def sumaMatriz(elemento,matriz):
    if isinstance(matriz,list) and matriz != [] and isinstance(elemento,int):
        return matriz1(elemento,matriz,len(matriz), len(matriz[0]),0, 0)
    else: return "La matriz no es una lista"

def matriz1(elemento, matriz,num_filas,num_columnas,fila,columna):
    if fila == num_filas:
        return matriz
    elif columna == num_columnas:
        return matriz_aux(elemento,matriz,num_filas,num_columnas,fila+1,0)
    else:
        return matriz_aux(elemento, matriz[fila][columna]+elemento, num_filas, num_columnas, fila, columna +1)
    
