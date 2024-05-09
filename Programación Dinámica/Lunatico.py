def construir_solucion(ganancias, optimos):
    elecciones = []
    d = len(ganancias)-1
    while(d >= 0):
        opt_ayer = optimos[d-1] 
        opt_anteayer = optimos[d-2] 
        valor_hoy = ganancias[d] if optimos[d] != 0 else float("-inf")
        if valor_hoy + opt_anteayer >= opt_ayer:
          elecciones.append(d)
          d -= 2
        else:
          d -= 1
    elecciones.reverse()
    return elecciones


def lunatico(ganancias):
    n = len(ganancias)
    if n == 0:return []
    if n == 1:return [0]
    if n == 2:return [0] if ganancias[0] > ganancias[1] else [1]

    #contando la primer casa
    dp_1 = [0] * n
    dp_1[0] = ganancias[0]
    dp_1[1] = max(ganancias[0], ganancias[1])
    for i in range(2, n - 1):
        dp_1[i] = max(dp_1[i - 1], dp_1[i - 2] + ganancias[i])

    #sin contar la primer casa
    dp_2 = [0] * n
    dp_2[0] = 0
    dp_2[1] = ganancias[1]
    for i in range(2, n):
        dp_2[i] = max(dp_2[i - 1], dp_2[i - 2] + ganancias[i])

    # Calcular la ganancia máxima total
    ganancia_maxima = dp_2[-1]
    optimos = dp_2
    if dp_1[-2] > dp_2[-1]:
        ganancia_maxima = dp_1[-2]
        optimos = dp_1
    
    return construir_solucion(ganancias, optimos)

"""
Ecuación de recurrencia: opt(i) = max(opt(i-1), opt(i-2) + gi) 
la cual nos dice que el óptimo con la casa i es la máxima ganancia entre el óptimo de hace dos casas
más la ganancia i o el óptimo hasta la última casa.

Complejidad: La complejidad del algoritmo es O(n) con n la cantidad de casas del arreglo,
ya que recorre dicho arreglo tres veces completas para solcionar el problema.
"""