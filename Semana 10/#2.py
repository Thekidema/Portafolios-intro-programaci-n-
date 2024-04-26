
calificaciones = [
    [45, 85, 70, 80],  
    [75, 30, 55, 90],  
    [85, 90, 95, 80],  
    [70, 32, 80, 85],  
    [80, 85, 40, 95]   
]

for i, estudiante in enumerate(calificaciones):
    nota_final = sum(estudiante) / len(estudiante)
    print(f"Nota final del estudiante {i+1}: {nota_final}")
