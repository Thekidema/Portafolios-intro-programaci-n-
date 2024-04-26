tiempo_total_vueltas = float(0) #ejercicio 1
tiempo_total_pits = float(0)

for i in range(10):
    tiempo_pit = input("Ingresa el tiempo de la pits: ")
    tiempo_pit = float(tiempo_pit)
    tiempo_vuelta = input("Ingresa el tiempo de los vuelta: ")
    tiempo_vuelta = float(tiempo_vuelta)
    
    tiempo_total_vueltas += tiempo_vuelta
    tiempo_total_pits += tiempo_pit

promedio_vuelta = tiempo_total_vueltas / 10
promedio_pits = tiempo_total_pits / 10

porcentaje_pits_vuelta = (promedio_pits / promedio_vuelta) * 100

print("Tiempo promedio por vuelta:", promedio_vuelta)
print("Tiempo promedio en pits:", promedio_pits)
print("Porcentaje en los pits por vuelta es", porcentaje_pits_vuelta, "%")