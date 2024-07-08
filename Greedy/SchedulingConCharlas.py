def charlas(horarios):
    #ordeno por hora de finalización
    horarios.sort(key=lambda x: x[1]) 
    sol = []
    if len(horarios) == 0:
        return []
    sol.append(horarios[0])
    for charla in horarios:
        if charla[0] >= sol[-1][1]:
            sol.append(charla)
    return sol

"""
La complejidad del algoritmo propuesto es el mismo orden de complejidad del algoritmo utilizado para ordenar, suponiendo un mergeSort O(nlogn)
"""