def cambio(monedas, monto):
    sol = []
    contador = 0
    for moneda in reversed(monedas):
        while contador + moneda <= monto:
            sol.append(moneda)
            contador += moneda
    return sol

"""
La complejidad del algortimo propuesto es O(C*M) con C la cantidad de monedas y M el monto, ya que en el peor de los casos pasamos por todas las monedas por lo menos una vez una cantidad M de veces.
El algoritmo no siempre da una solución óptima ya que por ejemplo en un sistema monetario con [1,3,4] para dar cambio de 6 nuestro algoritmo nos devuelve [4,1,1] y el óptimo en realidad es [3,3].
Es un algoritmo Greedy porque sigue o itera sobre una regla buscando un óptimo local acercandonos a un óptimo global.
"""