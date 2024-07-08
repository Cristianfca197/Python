# cada elemento i de la forma (valor, peso)
def mochila(elementos, W):
    elementos.sort(reverse = True, key = lambda x : x[0]/x[1])
    sol = []
    peso_act = 0
    for item in elementos:
        if peso_act + item[1] <= W:
            sol.append(item)
            peso_act += item[1]
    return sol

"""
La complejidad del algoritmo es O(nlogn) siendo la misma de ordenar los elementos por Valor/Peso de forma descendente, ya que luego solo recorremos los elementos para ir guardando los más valiosos por peso siempre que quepan en la mochila.
Este enfoque da la solución óptima siempre que se puedan guardar fracciones de los elementos, ya que máximizariamos el total del peso, siguiendo la regla de óptimo local para llegar al óptimo global, pero si no es el caso puede fallar.
"""