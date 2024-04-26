# Desarrolle un programa que muestre los números pares del 20 al 40 y a la par de cada número muestre su cuadrado.
numero = 20
while numero <= 40:  #se aplica ciclo while
    if numero % 2 == 0:
        print("Número par:", numero, "| Cuadrado:", numero ** 2)
    numero += 1
for numero in range(20, 41): #se aplica cico for 
    if numero % 2 == 0:
        print("Número par:", numero, "| Cuadrado:", numero ** 2)