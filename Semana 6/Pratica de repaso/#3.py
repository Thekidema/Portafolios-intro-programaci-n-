print()  #ejercicio 3#
resultado = int(0)
numero_ingresado = input("Ingresa un número para dividirlo entre sí 10 veces:")
numero_ingresado = int(numero_ingresado)
contador = 0
while contador < 10:
    resultado = numero_ingresado / numero_ingresado
    print("El resultado de dividir el número entre sí mismo es:", resultado)
    contador += 1
