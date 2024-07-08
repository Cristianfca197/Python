def sort(izq, der):
    sol = []
    i = 0
    d = 0
    while i < len(izq) and d < len(der):
        if izq[i] > der[d]:
            sol.append(der[d])
            d += 1
        else:
            sol.append(izq[i])
            i += 1
            
    while i < len(izq):
        sol.append(izq[i])
        i += 1
    while d < len(der):
        sol.append(der[d])
        d += 1
    
    return sol
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    medio = len(arr) // 2
    return sort(merge_sort(arr[:medio]), merge_sort(arr[medio:]))


"""
Con el Teorema maestro nos queda:
A(Cant. llamados recursivos) = 2
B(Proporcion de los llamados rec) = 2
C(Costos de partir y juntar) = O(n)
Y log2(2) = 1 = C -> O(n.log(n))= O(nlog(n))
"""