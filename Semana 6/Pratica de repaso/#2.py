n_menos_100 = int(0)
n_100_120 = int(0)
n_121_130 = int(0)
n_131_140 = int(0)
n_mas_140 = int(0)
altura_total = float(0)

cantidad = input("Ingresa la cantidad de niños para comparar alturas:")
cantidad = int(cantidad)

for x in range(cantidad):
    estatura_nino = input("¿Cuál es la estatura del niño (cm)?: ")
    estatura_nino = float(estatura_nino)
    if estatura_nino < 100:
        n_menos_100 += 1
    elif estatura_nino >= 100 and estatura_nino <= 120:
        n_100_120 += 1
    elif estatura_nino >= 121 and estatura_nino <= 130:
        n_121_130 += 1
    elif estatura_nino >= 131 and estatura_nino <= 140:
        n_131_140 += 1
    elif estatura_nino > 140:
        n_mas_140 += 1
    altura_total += estatura_nino
       
promedio_altura = altura_total / cantidad

print("El promedio de altura es:", promedio_altura)
print("Hay", n_menos_100, "niños que miden menos de 100 cm")
print("Hay", n_100_120, "niños que miden más de 100 cm y menos de 120 cm")
print("Hay", n_121_130, "niños que miden más de 121 cm y menos de 130 cm")
print("Hay", n_131_140, "niños que miden más de 131 cm y menos de 140 cm")
print("Hay", n_mas_140, "niños que miden más de 140 cm")
