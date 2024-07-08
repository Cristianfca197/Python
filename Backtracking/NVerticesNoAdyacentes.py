def no_adyacentes_BT(grafo, n, sol, visitados):
    if len(sol) == n:
        return sol

    for vertice in grafo.obtener_vertices():
        if vertice not in visitados:
            cumple = True
            for v in sol:
                if grafo.estan_unidos(vertice, v):
                    cumple = False
                    break
            if cumple:
                sol.append(vertice)
                visitados.append(vertice)
                for v in grafo.adyacentes(vertice):
                    visitados.append(v)
                resultado =  no_adyacentes_BT(grafo, n, sol, visitados)
                if resultado is not None:
                    return resultado
                #backtrack
                for v in grafo.adyacentes(vertice):
                    visitados.remove(v)
                visitados.remove(vertice)
                sol.remove(vertice)
    
    return None

def no_adyacentes(grafo, n):
    'Devolver una lista con los n vértices, o None de no ser posible'
    sol = []
    visitados = []
    return no_adyacentes_BT(grafo, n, sol, visitados)
    