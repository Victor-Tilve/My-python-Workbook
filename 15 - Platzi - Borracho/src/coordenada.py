'''
Created on 21/02/2021

@author: VATS
'''

class Coordenada:
    '''
    classdocs
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def mover(self, delta_x, delta_y):
        return Coordenada(self.x + delta_x, self.y + delta_y)
    
    def distancia(self, otra_coordenada):
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y
        #distancia euclidiana
        return (delta_x**2 + delta_y**2)**0.5