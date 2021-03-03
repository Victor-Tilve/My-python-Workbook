'''
Created on 14/02/2021

@author: VATS
'''

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saluda(self, otra_persona):
        return f'Hola, {otra_persona.nombre}, me llamo {self.nombre}'

# Uso

david = Persona('David', 35)
erika = Persona('Erika', 32)

print(david.saluda(erika))
