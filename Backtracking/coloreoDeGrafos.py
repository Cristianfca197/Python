def colorear_bt(grafo, colores, vertices, visitados):
    if len(visitados) == len(vertices):
        return True

    for vertice in vertices:
        if vertice not in visitados:
            for color in colores:
                color_valido = True
                for v in grafo.adyacentes(vertice):
                    if v in visitados and visitados[v] == color:
                        color_valido = False
                        break
                if color_valido:
                    visitados[vertice] = color
                    if  colorear_bt(grafo, colores, vertices, visitados):
                        return True
                    visitados.pop(vertice)
    return False

def colorear(grafo, n):
    visitados = dict()
    colores =  [i for i in range(n)]
    return colorear_bt(grafo, colores, grafo.obtener_vertices(), visitados)