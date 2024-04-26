precio_de_paga=float(input("Ingresa cuanto ganas por hora"))
Semanas_trabajadas=float(input("Ingrese las semanas trabajadas"))
salario_neto_mensual=Semanas_trabajadas*4.2*precio_de_paga
cargas_sociales=salario_neto_mensual*0.105
asociacion_solidarista=salario_neto_mensual*0.05
deducciones_totales=cargas_sociales+asociacion_solidarista
salario_completo_mensual=salario_neto_mensual-deducciones_totales

print("\nResumen del Salario:")
print(f"Salario Bruto Mensual: ₡{salario_neto_mensual:.2f}")
print(f"Deducciones totales: -₡{deducciones_totales:.2f}")
print(f"Salario Neto Mensual: ₡{salario_neto_mensual:.2f}")