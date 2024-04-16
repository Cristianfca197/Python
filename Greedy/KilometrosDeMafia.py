# pedidos: lista de tuplas con (km inicio, km fin)
def hay_interseccion(anterior, nuevo):
    return anterior[1] > nuevo[0]

def asignar_mafias(pedidos):
    pedidos.sort(key = lambda x: x[1])
    asignaciones = []
    for pedido in pedidos:
        if len(asignaciones) == 0 or not hay_interseccion(asignaciones[-1], pedido):
            asignaciones.append(pedido)
    return asignaciones

"""
Es un algoritmo greedy ya que tenemos una regla sencilla con una solución parcial que nos acerca a la solución final la cual aplicamos iterativamente

El orden del algoritmo es O(ordenamiento) que suponemos O(nlogn) ya que luego del mismo solo recorremos la lista una vez y vamos agregando o no el pedido según nuestra regla
"""