#En una sala de teatro se requiere almacenar los nombres de las personas 
#que ocuparán las butacas de una fila, cada fila tiene 10 butacas. Cree 
#un programa que almacena los nombres en las posiciones que le van 
#indicando, por ejemplo: Ana Jiménez, 4 (el cuatro indica el número de 
#butaca)


butacas = [''] * 10     #lista para representar las 10 butacas

nombre1 = input("Ingrese el nombre de la persona para la butaca 1: ")
butacas[0] = nombre1

nombre2 = input("Ingrese el nombre de la persona para la butaca 2: ")
butacas[1] = nombre2

nombre3 = input("Ingrese el nombre de la persona para la butaca 3: ")
butacas[2] = nombre3

nombre4 = input("Ingrese el nombre de la persona para la butaca 4: ")
butacas[3] = nombre4

nombre5 = input("Ingrese el nombre de la persona para la butaca 5: ")
butacas[4] = nombre5

nombre6 = input("Ingrese el nombre de la persona para la butaca 6: ")
butacas[5] = nombre6

nombre7 = input("Ingrese el nombre de la persona para la butaca 7: ")
butacas[6] = nombre7

nombre8 = input("Ingrese el nombre de la persona para la butaca 8: ")
butacas[7] = nombre8

nombre9 = input("Ingrese el nombre de la persona para la butaca 9: ")
butacas[8] = nombre9

nombre10 = input("Ingrese el nombre de la persona para la butaca 10: ")
butacas[9] = nombre10
print("\nLista de butacas ocupadas:")
for i in range(10):                         #mostrar listas de las 10 butacas 
    if butacas[i] != '':
        print(f"Butaca {i+1}: {butacas[i]}")
