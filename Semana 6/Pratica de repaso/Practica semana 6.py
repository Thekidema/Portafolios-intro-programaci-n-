temperatura_por_dia = {} #DATOS DEL EJERCICIO/VARIABLES USADAS
temperatura_maxima_por_persona = {}
temperatura_minima_por_persona = {}
dias_a_la_semana = ["Lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]
def calcular_promedio(temperatura):
    return sum(temperatura) / len(temperatura) if len(temperatura) > 0 else 0

for dia in dias_a_la_semana:
    temperaturas = []
    while True:
        nombre = input(f"Ingrese el nombre de la persona que ingresa por día {dia}: ")
        temperatura = float(input(f"Ingrese la temperatura de {nombre}: "))
        temperaturas.append(temperatura)

        if input("¿Desea ingresar otra temperatura? (si/no): ").lower() != 'si':
            break
    # MAXIMO Y MINIMO FUERA DEL BUCLE 
    temperatura_promedio = calcular_promedio(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)
    temperatura_por_dia[dia] = temperatura_promedio
    temperatura_maxima_por_persona[dia] = (nombre, temperatura_maxima)
    temperatura_minima_por_persona[dia] = (nombre, temperatura_minima)
# RESULTADOS DEL PROGRAMA
print("\nResultados:")
for dia in dias_a_la_semana:
    print(f"\n{dia}:")
    print(f"Temperatura promedio: {temperatura_por_dia[dia]:.2f}")
    print(f"Persona con la temperatura más alta: {temperatura_maxima_por_persona[dia][0]} ({temperatura_maxima_por_persona[dia][1]}°C)")
    print(f"Persona con la temperatura más baja: {temperatura_minima_por_persona[dia][0]} ({temperatura_minima_por_persona[dia][1]}°C)")
    print("muchas gracias hasta luego")
