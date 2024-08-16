word = input("Ingrese una palabra: ")

for i in range(10):
    print(word)
    
print("Segunda operación")

contador = 1

for i in [1,3,4]:
    print(f'Vuelta número {contador}')
    print(f'Hola, ahora i vale {i} y su cuadrado es {i ** 2}')
    contador += 1 
