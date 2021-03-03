def funcion_decoradora(funcion):
    def wrapper():
        print('Este es el ultimo mensaje')
        funcion()
        print('Este es el primer mensaje')
    return wrapper()

def zumbido():
    print('Buzzzz')


if __name__ == '__main__':
    zumbido = funcion_decoradora(zumbido)