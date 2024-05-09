import copy

def vertex_cover_min_rec(grafo, lista_solucion):
    vertices = grafo.obtener_vertices()
    if len(vertices) == 0:
        return 

    vertice_actual = max(vertices, key = lambda x: len(grafo.adyacentes(x)))
    vertices_adyacentes = grafo.adyacentes(vertice_actual)

    if len(vertices_adyacentes) == 0:
        for vertice in grafo.obtener_vertices():
            grafo.borrar_vertice(vertice)
        return 

    for vertice in vertices_adyacentes:
        grafo.borrar_arista(vertice_actual, vertice)
    
    lista_solucion.append(vertice_actual)
    vertex_cover_min_rec(grafo, lista_solucion)



def vertex_cover_min(grafo):
    lista_solucion = []
    copia_grafo = copy.deepcopy(grafo)
    vertex_cover_min_rec(copia_grafo, lista_solucion)
    return lista_solucion