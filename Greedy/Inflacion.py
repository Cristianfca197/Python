def precios_inflacion(R):
    R.sort(reverse = True)
    sol = 0
    for i in range(len(R)):
        sol += pow(R[i], i+1)
    return sol

"""
La complejidad del algoritmo propuesto es O(nlogn) misma complejidad de ordenar los precios de los productos de mayor a menor, para así ir comprando día a día el producto más costoso y por ende el producto que en valor total más crece con la inflación, por lo que siempre nos da solución óptima en este problema, además es un algortimo Greedy por iterar sobre una regla, para llegar a óptimo locales para un óptimo global.
"""