def elemento_desordenado_rec(inicio, fin, arr):
    if inicio == fin:
        return None
    medio = (fin+inicio) // 2
    if arr[medio] < arr[inicio] or arr[medio] > arr[fin]:
        return arr[medio]
    else:
        izq = elemento_desordenado_rec(inicio, medio, arr)
        der = elemento_desordenado_rec(medio+1, fin, arr)
        return izq if izq != None else der


def elemento_desordenado(arr):
    medio = len(arr) // 2
    izq = elemento_desordenado_rec(0, medio, arr)
    der = elemento_desordenado_rec(medio, len(arr)-1, arr)
    return izq if izq != None else der

"""El orden para es O(n), ya que no podemos separa las busqueda en alguna de las partes y en el peor de los casos terminamos recorriendo el arreglo entero"""