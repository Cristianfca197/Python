def fibonacci(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    fibo = (n+1) * [1]
    for n in range(2, n+1):
        fibo[n] = fibo[n-1]+fibo[n-2]
    return fibo[n]