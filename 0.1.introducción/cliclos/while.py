contador = 0

print("CALCULADORA DE MASA CORPORAL")
while contador != 2:
    contador = int(input("¿Quieres calcular el IMC? 1. SI, 2. NO: "))

    if contador == 1:
        estatura = float(input("Ingrese su estatura : "))
        peso = float(input("Ingrese peso en kilogramos : "))
        resultado = round(peso/(estatura * estatura))
        if resultado < 18.5:
            print(f'IMC {resultado} = BAJO DE PESO')
        elif 18.5 < resultado < 24.99:
            print(f'IMC {resultado} = PESO NORMAL')
        elif 25 < resultado < 30:
            print(f'IMC {resultado} = SOBRESO')
        elif resultado > 30:
            print(f'IMC {resultado} = OBESIDAD') 
    elif contador == 2 :
        print("Hasta pronto")

