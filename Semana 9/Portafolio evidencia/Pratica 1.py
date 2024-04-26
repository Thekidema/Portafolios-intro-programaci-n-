#Eduardo es un joven ciclista, cada semana debe reportar a su entrenador la cantidad de kilómetros recorridos en sus prácticas. Haga un programa que le permita almacenar para cada día los kilómetros recorridos y luego al final de la semana muestre por cada día, junto con l toal de la semana. Para la solución, utilice arreglos y ciclos
# Definir arreglo para almacenar los kilómetros recorridos por día
kilometros_por_dia = [0] * 7  # Inicialmente, se asume que no ha recorrido nada cada día

# Primero ingreso los ciclos por dia utilizando un for, in utilizando un rango de 7
for dia in range(7):
    kilometros = float(input(f"Ingrese los kilómetros totales recorridos en el día {dia + 1}: "))
    kilometros_por_dia[dia] = kilometros

# Luego se saca el total de los kilometros recorridos en el transcurso de los 7 dias
total_semana = 0
for dia in range(7):
    total_semana += kilometros_por_dia[dia]
    print(f"Día {dia + 1}: {kilometros_por_dia[dia]} kilómetros")

print(f"Total de kilómetros recorridos en la semana: {total_semana} kilómetros")
