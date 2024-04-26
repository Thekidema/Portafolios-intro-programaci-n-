ingreso_mensual=float(input("Digite el ingreso generado por mes"))
gastos_mensuales=float(input("Ingresa los gastos generados por mes"))
porcentaje_gastos=(gastos_mensuales/ingreso_mensual)*100
porcentaje_disponible=100-porcentaje_gastos
print(f"\nporcentaje de gatos por alimentacion:{porcentaje_gastos:.2f}%")
print(f"Porcentaje disponible para otros rubros: {porcentaje_disponible:.2f}%")