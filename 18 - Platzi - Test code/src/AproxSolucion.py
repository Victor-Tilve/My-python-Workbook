'''
Created on 13/02/2021
Aproximacion de solucion cuando sea necesario 
dar una respuesta al problema
@author: VATS
'''

if __name__ == '__main__':
    objetivo = int (input('Escoge un numero entero: '))
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.0
    
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso
        
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada {objetivo}')
    else:
        print(f'La raiz cuadrada es: {respuesta}')
    