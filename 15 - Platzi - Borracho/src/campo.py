'''
Created on 21/02/2021

@author: VATS
'''


class Campo:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.coordenadas_de_borrachos = {}
    
    def anadir_borracho(self,borracho, coordenada):
        '''
        recibe un borracho y una coordenada para ser 
        agregado en el diccionario
        '''
        self.coordenadas_de_borrachos[borracho] = coordenada
        
    def mover_borracho(self, borracho):
        delta_x, delta_y = borracho.camina()
        coordenada_actual = self.coordenadas_de_borrachos[borracho]
        nueva_coordenada = coordenada_actual.mover(delta_x,delta_y)
        
        self.coordenadas_de_borrachos[borracho] = nueva_coordenada
        
    def obtener_coordenada(self, borracho): 
        return self.coordenadas_de_borrachos[borracho]   
    