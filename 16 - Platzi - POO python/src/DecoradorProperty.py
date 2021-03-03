'''
Created on 14/02/2021

@author: VATS
'''

class Millas:
    def __init__(self):
        self._distancia = 0
    #Funcion para obtener el valor de _distancia
    #usando el decorador property
    @property
    def obtener_distancia(self):
        print('llamada al metodo getter')
        return self._distancia
    
    #Funcion para definir el valor de _distancia
    @obtener_distancia.setter
    def obtener_distancia(self, valor):
        if valor < 0:
            raise ValueError('No es posible converti distancias menores a 0')
        print('Llamada de metodo setter')
        self._distancia = valor

# Crear un objeto nuevo

avion = Millas()

# Indicar la distancia
avion.obtener_distancia = 20

# Obtener atributo distancia
print(avion.obtener_distancia)




if __name__ == '__main__':
    pass