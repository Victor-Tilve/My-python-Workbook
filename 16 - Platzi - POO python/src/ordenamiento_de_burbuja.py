'''
Created on 15/02/2021

@author: VATS
'''
import random

def ordenamiento_de_burbuja(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista    

if __name__ == '__main__':
    tamanio_de_lista = int(input('De que tamanio sera la lista? '))
    
    _lista = [random.randint(0,100) for i in range(tamanio_de_lista)]    
    print(_lista)
    
    Lista_ordenada = ordenamiento_de_burbuja(_lista)
    
    print(_lista) # Pasa por referencia?
    print(Lista_ordenada)
