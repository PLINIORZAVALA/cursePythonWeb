'''
def suma(a,b,c):
    return a+b+c
suma(3,5,6)
print(suma)
'''

'''
def suma(*args):
    s = 0
    for arg in args:
        s += arg
    return s

resultado = suma(3,5,6)
print(resultado)
'''

def lenguaje(nombre, *lenguajes):
    print(f'Hola: {nombre}')
    print(f'Tus lengujes favoritos son: {lenguajes}')

resultado = lenguaje("Max","Rubi","Laravel","PHP")
