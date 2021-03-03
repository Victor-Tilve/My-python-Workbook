'''
Created on 14/02/2021

@author: VATS
'''

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def avanza(self):
        print('Ando caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def avanza(self):       #Polimorfismo
        print('Me muevo en bicicleta')
    
def main():
    persona = Persona('David')
    persona.avanza()
    
    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__ == '__main__':
    main()
        