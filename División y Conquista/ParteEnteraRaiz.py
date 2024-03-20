def calcular_raiz(inicio, final, n):
    if inicio <= final:
        mitad = (inicio + final) // 2
        cuadrado = mitad * mitad

        if cuadrado == n:
            return mitad
        elif cuadrado < n:
            return calcular_raiz(mitad + 1, final, n)
        else:
            return calcular_raiz(inicio, mitad - 1, n)
    else:
        return final

def parte_entera_raiz(n):
    if n <= 1:
        return n
    return calcular_raiz(0, n//2, n)

print(parte_entera_raiz(10))
print(parte_entera_raiz(25))

#El orden del algoritmo es O(log n) ya que en cada iteración se reduce el intervalo a evaluar a la mitad como en la búsqueda binaria.