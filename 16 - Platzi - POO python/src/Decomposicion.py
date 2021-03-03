'''
Created on 14/02/2021

@author: VATS
'''

class Automovil:
    def __init__(self,modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado =  'En_reposo'
        self._motor = Motor(cilindros = 4)
    
    def acelerar (self, tipo = 'despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'En marcha'

class Motor:
    def __init__(self,cilindros, tipo = 'gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
    def inyecta_gasolina(self,cantidad):
        pass

if __name__ == '__main__':
    pass