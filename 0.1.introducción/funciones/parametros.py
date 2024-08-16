def es_par(numero):
    if(numero % 2):
        print(f'El número {numero} es par')
    else:
        print(f'El número {numero} es no es par')
        
#Asignamos el valor al parametro
es_par(22)

def multiplicacion(numero = None):
    if numero == None:
        print("Por favor, introduce un número: ")
    else:
        print(f'TABLA DE MULTIPLICAR DEL {numero}')
        for i in (1,11):
            print(f'{i} * {numero} = {í * numero}')

#Asignamos del parametro para realizar la multiplicación
multiplicacion(10)