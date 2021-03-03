'''
Created on 14/02/2021

@author: VATS
'''

class Rectangulo:
    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura
    
    def area(self):
        return self.__base * self.__altura
    
class Cuadrado(Rectangulo): #forma en que aplico herencia
    
    def __init__(self,lado):
        super().__init__(lado, lado)   
    
if __name__ == '__main__':
    rectangulo = Rectangulo(base = 3, altura = 4)
    print(rectangulo.area())
    
    cuadrado = Cuadrado(lado = 5)
    print(cuadrado.area())