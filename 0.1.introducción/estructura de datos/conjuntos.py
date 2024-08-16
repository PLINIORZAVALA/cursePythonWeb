'''
Metodos:
    add
    clear
    pop
    remove
    union
'''

alumnos = {"Andrea", "Ruby", "Marcos", "Marlon", "Jose"}

lenguajes = set(["PHP","Java","C","Python"])

'''
lenguajes.add()
lenguajes.pop()
lenguajes.clear()
'''

lenguajes_union = alumnos.union(lenguajes)
print(lenguajes_union)