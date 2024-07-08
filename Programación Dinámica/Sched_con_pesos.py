def sche_solucion(max_valor, charlas, p, j, solucion):
   if j == 0:
       return solucion
   if charlas[j-1][2]+max_valor[p[j]] >= max_valor[j-1]:
       solucion.append(charlas[j-1])
       return sche_solucion(max_valor, charlas, p, p[j], solucion)
   else:
       return sche_solucion(max_valor, charlas, p, j-1, solucion)

def sche_dinamico(p, charlas):
    max_valor = (len(charlas)+1) * [0]
    for j in range(1, len(max_valor)):
        max_valor[j] = max(charlas[j-1][2] + max_valor[p[j]], max_valor[j-1])
    return sche_solucion(max_valor, charlas, p, len(max_valor)-1, [])

def scheduling(charlas):
    if len(charlas) == 0:
        return []
    #ordeno por orden de fin
    charlas.sort(key = lambda x: x[1])
    p = (len(charlas)+1) * [0]
    for n in range(1, len(p)):
        for i in range(0, n):
            if charlas[n-1][0] >= charlas[i][1]:
                p[n] = i+1
    return sche_dinamico(p, charlas)[::-1]

"""
La complejidad del algoritmo planteado es O(nlon), ya que ordenar las charlas es O(nlogn), obtener P(arreglo con los indices de las ultimas charla superpuesta para la charla i) O(nlogn), calcular Max_valor(maximo valor consideranto hasta la charla i) O(n), por lo que nos queda O(nlogn)
"""