import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

def es_bipartito(grafo):
    grupoS, grupoT = set(), set()

    for vertice in grafo.vertices():
        if vertice in grupoT:
            for adyacente in grafo.adyacentes(vertice):
                if adyacente in grupoT:
                    return False
                grupoS.add(adyacente)
        else:
            grupoS.add(vertice)
            for adyacente in grafo.adyacentes(vertice):
                if adyacente in grupoS:
                    return False
                grupoT.add(adyacente)

    return True