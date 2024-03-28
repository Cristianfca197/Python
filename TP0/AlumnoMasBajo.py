def indice_mas_bajo_rec(inicio, fin, alumnos):
    mid = inicio + (fin-inicio) // 2

    if (fin - inicio) == 1:
        if alumnos[inicio].altura < alumnos[fin].altura:
            return inicio
        else:
            return fin
    
    if alumnos[mid].altura > alumnos[mid+1].altura:
        return indice_mas_bajo_rec(mid, fin, alumnos)
    elif alumnos[mid].altura < alumnos[mid+1].altura:
        return indice_mas_bajo_rec(inicio, mid, alumnos)
    else:
        return mid
    

    

def indice_mas_bajo(alumnos):
    return indice_mas_bajo_rec(0, len(alumnos) - 1, alumnos)


def validar_mas_bajo(alumnos, indice):
    return alumnos[indice - 1].altura > alumnos[indice].altura < alumnos[indice + 1].altura