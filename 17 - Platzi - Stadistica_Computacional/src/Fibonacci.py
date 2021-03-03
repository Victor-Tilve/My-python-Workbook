'''
Created on 20/02/2021

@author: VATS
'''

def fibonacci (n, memo = {}):
    if n == 0 or n == 1:
        return 1
    
    try:
        return memo[n] # Pedir perdon en vez de pedir permiso
    except KeyError:
        resultado = fibonacci(n - 1, memo) + fibonacci(n -2, memo)
        return resultado

if __name__ == '__main__':
    n = int(input('Escoge un numero: '))
    resultado = fibonacci(n) #un solo parametro, la lista sse toma como parametro por defecto
    print(resultado)
    
    