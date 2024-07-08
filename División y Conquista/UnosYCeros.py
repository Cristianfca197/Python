def indice_primer_cero_rec(inicio, fin, arr):
    if inicio == fin:
        return None
    medio = (inicio + fin) // 2

    if arr[medio] == 0:
        if arr[medio-1] != 0:
            return medio
        else:
            return indice_primer_cero_rec(inicio, medio, arr)
    else:
        return indice_primer_cero_rec(medio+1, fin, arr)

def indice_primer_cero(arr):
    if arr[0] == 0:
        return 0
    medio = len(arr) // 2
    izq = indice_primer_cero_rec(0, medio, arr)
    der = indice_primer_cero_rec(medio, len(arr)-1, arr)
    return izq if izq != None else der if der != None else -1