#Desarrolle un programa que le indique si su año de nacimiento es en año bisiesto
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
if (anio_nacimiento % 4 == 0 and anio_nacimiento % 100 != 0) or (anio_nacimiento % 400 == 0):
    print(f"El año {anio_nacimiento} es un año bisiesto.")
else:
    print(f"El año {anio_nacimiento} no es un año bisiesto.")
