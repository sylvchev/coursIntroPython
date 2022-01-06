from __future__ import print_function

# Module nombres de Fibonacci
def fib(n):    # ecrit la serie de Fibonacci jusqu'a n
    a, b = 0, 1
    while b < n:
        print (b, end=' ')
        a, b = b, a+b
        
def fib2(n): # retourne la serie de Fibonacci jusqu'a n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
