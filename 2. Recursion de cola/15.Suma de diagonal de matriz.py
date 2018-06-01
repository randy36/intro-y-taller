def sumarDiagonal(matriz):
    if isinstance(matriz,list) and matriz != []:
        return sumarDiagonal1(matriz, len(matriz), 0, 0)
    else: return " Error no es una lista"

def sumarDiagonal1(matriz,filas,indice2, resultado):
    if indice2==filas:
        return resultado
    else: return sumarDiagonal1(matriz,filas,indice2+1,resultado +matriz[indice2][indice2])
