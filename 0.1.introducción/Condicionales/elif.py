edad = int(input("Ingrese su edad : "))

if edad < 16 :
    print("No tienes la edad necesaria para conducir")
elif edad < 18 :
    print("Puedes obtener un permiso para conducir")
elif edad < 70 :
    print("Puedes obtener una licencia estandar")
else:
    print("Necesitas obtener una licencia especial")