def maximo(cant_personas, num_fila, num_columna, fila_anterior):
    if num_fila == 0:
        return 0
    if num_columna < cant_personas:
        return fila_anterior[num_columna]
    return max(fila_anterior[num_columna], fila_anterior[num_columna-cant_personas]+cant_personas)

def bodegon_dinamico(P, W):
    filas = len(P)+1
    columnas = W+1
    matriz = [[0]*columnas for _ in range(filas)]
    
    for fila in range(filas):
        for columna in range(columnas):
            matriz[fila][columna] = maximo(P[fila-1], fila, columna, matriz[fila-1])
 
    solucion = []
    fila, columna = filas-1, columnas-1
    while fila != 0 and columna != 0:
        pos_actual = matriz[fila][columna]
        if  pos_actual != matriz[fila-1][columna] and matriz[fila-1][columna-P[fila-1]] + P[fila-1] == pos_actual: 
            solucion.append(P[fila-1])
            columna = columna - P[fila-1]
        fila -= 1

    solucion.reverse()
    return solucion
    
"""
Complejidad: O(#cant_grupos * capacidad)
Pero al resolverlo con la misma idea del problema de la mochila con solución de programación dinámica, sabemos que capacidad en realidad se escribe como 2^m con m la longitud de lectura del valor de W, dandonos como resultados una complejidad O(#cant_grupos * 2^m) siendo esta una complejidad exponencial
"""