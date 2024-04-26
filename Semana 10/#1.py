# Datos de ventas mensuales por producto (filas) y por mes (columnas)
ventas = [[100, 80, 150],
          [120, 90, 160],
          [130, 100, 170]]
total_ventas_por_producto = [sum(producto) for producto in ventas]
total_ventas_por_mes = [sum(ventas[i][j] for i in range(len(ventas))) for j in range(len(ventas[0]))]

print("Total de ventas por producto:", total_ventas_por_producto)
print("Total de ventas por mes:", total_ventas_por_mes)