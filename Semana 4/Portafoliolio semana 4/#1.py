#Desarrolle un programa que muestre el mayor de dos números.
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if numero1 > numero2:
    mayor_dos_numeros = numero1
else:
    mayor_dos_numeros = numero2
print("El mayor de los dos números es:", mayor_dos_numeros)

numero3 = float(input("Ingrese el tercer número: "))
numero4 = float(input("Ingrese el cuarto número: "))

mayor_cuatro_numeros = numero1
if numero2 > mayor_cuatro_numeros:
    mayor_cuatro_numeros = numero2
if numero3 > mayor_cuatro_numeros:
    mayor_cuatro_numeros = numero3
if numero4 > mayor_cuatro_numeros:
    mayor_cuatro_numeros = numero4
print("El mayor de los cuatro números es:", mayor_cuatro_numeros)
