'''
Created on 17/02/2021

@author: VATS
'''
import random

def ordenamiento_por_mezcla(lista):
    if len(lista) >  1:
        medio = len(lista)//2
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(izquierda, '*' * 5, derecha)
        #llamada recursiva
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        #Iterador para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador para las lista principal
        k = 0
        
        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1
            
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1
        print(f'izquierda {izquierda}, Derecha {derecha}')
        print(lista)
        print('-' * 50)
        return lista
            
            
        
if __name__ == '__main__':
    tamanio_de_lista = int(input('De que tamanio sera la lista? '))
    
    _lista = [random.randint(0,100) for i in range(tamanio_de_lista)]    
    print(_lista)
    print('-'*30)
    
    Lista_ordenada = ordenamiento_por_mezcla(_lista)
    
    print(_lista) # Pasa por referencia?
    print(Lista_ordenada)
