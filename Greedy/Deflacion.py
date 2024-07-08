def precios_deflacion(R):
    R.sort()
    sol = 0
    for i in range(len(R)):
        sol += R[i] / (2**i)
    return sol

"""
La complejidad del algoritmo propuesto es O(nlogn) misma complejidad de ordenar los precios de los productos de menor a mayor, para así ir comprando día a día el producto menos costoso y por ende el producto que en valor total menos decrece con la deflación, por lo que siempre nos da solución óptima en este problema, además es un algortimo Greedy por iterar sobre una regla, para llegar a óptimo locales para un óptimo global.
"""