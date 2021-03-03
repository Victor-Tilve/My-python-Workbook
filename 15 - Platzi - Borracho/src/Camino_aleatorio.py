'''
Created on 21/02/2021

@author: VATS
'''
from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada
from numpy import round


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        
    return inicio.distancia(campo.obtener_coordenada(borracho))    
    
def simular_caminata(pasos, numero_de_intentos, tipo_de_borrachos):
    borracho = tipo_de_borrachos(nombre = 'Victor')
    origen = Coordenada(0,0)
    distancias = []
    
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    
    return distancias

def main(distancias_de_caminata, numero_de_intentos, tipo_de_borracho):
    for pasos in distancias_de_caminata:
        distancias = simular_caminata(pasos, numero_de_intentos, tipo_de_borracho)
        distancias_medias = round(sum(distancias)/len(distancias),4)
        distancia_maxiama = max(distancias)
        distancia_minima = min(distancias)
        
        print(f'{tipo_de_borracho.__name__} caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancias_medias}')
        print(f'Maxima = {distancia_maxiama}')
        print(f'Minima = {distancia_minima}')

if __name__ == '__main__':
    distancias_de_caminata = [10, 100, 1000, 10000]
    numero_de_intentos = 10
    main(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)