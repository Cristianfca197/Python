def problema_soga(n):
    resultado = [1]*(n)
    for i in range(1, n):
        max = resultado[i]
        
        resto, mitad = (i+1)%2 ,(i+1)//2
        if resto > 0:
            if mitad*(mitad+resto) > max:
                max = mitad*(mitad+resto)
        else:
            if mitad*mitad > max:
                max = mitad*mitad
        
        for j in range(i-1, mitad-1, -1):
            if resultado[j]*(i-j) > max:
                max = resultado[j]*(i-j)
            
        resultado[i] = max
    return resultado[n-1]

"""
La complejidad del algoritmo es O(n^2) con n el número a calcular, ya que va calculando la solucion iterativamente en un arreglo de largo n y por cada nueva posición recorre el arreglo hasta la posicion n/2 en sentido contrario. Probablemente se pueda mejorar si se demuestra que desde cierto n es posible empezar a comprar con soluciones más cercanas y no hasta n/2
"""