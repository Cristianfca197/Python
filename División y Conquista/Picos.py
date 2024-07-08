def posicion_pico(v, ini, fin):
    medio = (ini+fin) // 2
    if v[medio-1] < v[medio] and v[medio] > v[medio+1]:
        return medio
    if v[medio-1] > v[medio]:
        return posicion_pico(v, ini, medio)
    return posicion_pico(v, medio+1, fin)

"""
Con el Teorema maestro nos queda:
A(Cant. llamados recursivos) = 2
B(Proporcion de los llamados rec) = 2
C(Costos de partir y juntar) = O(1)
Y log2(2) = 1 = C -> O(1.log(n))= O(log(n))
"""