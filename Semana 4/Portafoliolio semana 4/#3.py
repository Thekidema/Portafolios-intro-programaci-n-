#Desarrolle un programa que ordene de forma descendente 3 números.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
maximo = max(num1, num2, num3)
minimo = min(num1, num2, num3)
medio = (num1 + num2 + num3) - maximo - minimo 
print("Los números ordenados de forma descendente son:", maximo, medio, minimo)
