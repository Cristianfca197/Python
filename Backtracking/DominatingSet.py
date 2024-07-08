def dominating_set_min_bt(grafo, vertices, visitados, lista_solucion):
    if not vertices:
        return

    if len(visitados) == len(grafo.obtener_vertices()):
        return

    vertice_actual = max(vertices.items(), key = lambda x: x[1])[0]

    if vertice_actual not in visitados:
        visitados.append(vertice_actual)
        lista_solucion.append(vertice_actual)
        
        for vertice in grafo.adyacentes(vertice_actual):
            if vertice not in visitados:
                visitados.append(vertice)
                vertices[vertice] -= 1
                for vertice_adyacente in grafo.adyacentes(vertice):
                    if vertice_adyacente in vertices:
                        vertices[vertice_adyacente] -= 1

    vertices.pop(vertice_actual)
    dominating_set_min_bt(grafo, vertices, visitados, lista_solucion)

def dominating_set_min(grafo):
    lista_solucion = []
    vertices = {}
    visitados = []

    for vertice in grafo.obtener_vertices():
        vertices[vertice] = len(grafo.adyacentes(vertice))

    dominating_set_min_bt(grafo, vertices, visitados, lista_solucion)

    return lista_solucion