def operaciones(k):
    cant_operaciones = [0] * (k+1)
    operaciones = [''] * (k+1)
    
    for i in range(1, k+1):
        cant_operaciones[i] = cant_operaciones[i-1] + 1
        operaciones[i] = 'mas1'
        
        if i%2 == 0 and cant_operaciones[i//2] + 1 < cant_operaciones[i]:
            cant_operaciones[i] = cant_operaciones[i//2] + 1
            operaciones[i] = 'por2'
    
    resultado = []
    while k > 0:
        if operaciones[k] == 'mas1':
            resultado.append('mas1')
            k -= 1
        else:
            resultado.append('por2')
            k //= 2
    
    resultado.reverse()       
    return resultado

"""
Ecuación de recurrencia: 
cant_operaciones[k] = min(cant_operaciones[k-1] +1 , cant_oepraciones[k//2] + 1)
Complejidad:
la complejidad del algoritmo es O(K) con k el número a calcular, ya que vamos calculando las soluciones de los números anteriores de forma iterativa, con una idea de fibonacci 
"""