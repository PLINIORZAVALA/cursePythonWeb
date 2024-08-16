# Primera forma de crear un diccionario

diccionario = {
    "Nombre" : "Max",
    "Edad" : 22,
    "Documento" : 3456547
}

print(diccionario)

# Segunda forma de crear un diccionario
sec_diccionario = dict(nombre = 'Paola',
                       Edad = 37,
                       Documento = 34567890)

print(sec_diccionario)

# Tercera forma de crear un diccionario
ter_diccionario = dict([
    ('Nombre', 'Jose'),
    ('Edad', 23),
    ('Documento',567890)
])

