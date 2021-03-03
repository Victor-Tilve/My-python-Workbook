'''
Created on 21/02/2021

@author: VATS
'''
import random

class Borracho:
    '''
    classdocs
    '''
    def __init__(self, nombre):
        self.nombre = nombre

class BorrachoTradicional(Borracho):
    
    def __init__(self, nombre):
        '''
        Constructor
        '''
        super().__init__(nombre)
    
    def camina(self): #retorna una tupla
        return random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        