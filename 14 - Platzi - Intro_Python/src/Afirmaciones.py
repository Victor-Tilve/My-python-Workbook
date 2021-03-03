'''
Created on 14/02/2021

@author: VATS
'''

def primera_letra(lista_de_palabras):
    primeras_letras = []
    
    for palabra in lista_de_palabras:
        
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'
        
        primeras_letras.append(palabra[0])
        
    return primeras_letras

lista_de_palabras = ['victor', 'Alfonso']

print(primera_letra(lista_de_palabras))