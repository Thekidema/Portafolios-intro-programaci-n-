#Desarrolle un programa que permita determinar la nota mayor, la nota menor, la cantidad de aprobados y la cantidad de reprobados de un grupo de alumnos. Muestre los resultados obtenidos.
 #Notas: No se conoce la cantidad de alumnos.La nota de aprobación es 70.
#variables usadas 
nota_mayor = float('-inf')  
nota_menor = float('inf')   
cantidad_aprobados = 0
cantidad_reprobados = 0
terminado = False

while not terminado:
    nota = float(input("Ingrese la nota del alumno (o ingrese -1 para finalizar): "))
    
    if nota == -1:
        terminado = True        # condicional que aplica el fin del ciclo 
    else:
        
        if nota > nota_mayor:
            nota_mayor = nota
        if nota < nota_menor:
            nota_menor = nota
         
        if nota >= 70:
            cantidad_aprobados += 1      # se aplica la cantida de reprobados
        else:
            cantidad_reprobados += 1

print("\nResultados:")
print("Nota mayor:", nota_mayor) #los prints que muestran la notas de los alumnos 
print("Nota menor:", nota_menor)
print("Cantidad de aprobados:", cantidad_aprobados)
print("Cantidad de reprobados:", cantidad_reprobados)
