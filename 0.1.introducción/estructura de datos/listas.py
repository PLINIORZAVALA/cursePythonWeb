
'''
asignaturas = ["Ingles","Matematica","Fisica"]
print(asignaturas[0])
'''

numero = []
for i in range(6):
    numero.append(int(input("Ingrese números a la lista")))

print(f'Los números ganadores son: {numero}')

#Metodos para alterar el resultado de la lista
desendente = numero.sort()
print(f'Los números ordenados en forma descendente son: {desendente}')