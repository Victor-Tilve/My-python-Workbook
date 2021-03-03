def funcion_decoradora(funcion):
    def wrapper():
        print("Hols")
        funcion()
        print("Chao")
    return wrapper()
  


@funcion_decoradora
def zumbido():
    print('Buzzzz')


if __name__ == '__main__':
    _zumbido = zumbido