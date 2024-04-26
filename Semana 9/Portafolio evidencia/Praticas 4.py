#Jimena es una joven que trabaja para pagarse sus estudios. Se ha 
#inscrito en una de las plataformas de entrega de comida y otros. 
#Haga un programa que le permita a Jimena registrar el monto ganado 
#en cada día, al finalizar la semana le mostrará el total y le indicará el día 
#que ganó menos dinero

montoganado = []        # se crea una lista 

                        # Registro de los montos ganados por día
for dia in range(1, 8): # aunque el valor sea 8 solo se contara 7 que son el total de dias de la semana 

    monto = float(input(f"Ingrese el monto ganado el día {dia}: "))  #Registros que obtuve  de los montos que gano por dia jimena 
    montoganado.append(monto)


total_semana = sum(montoganado)    #esto me ayuda a calcular el total de ganado durante la semana 


dias_malos = montoganado.index(min(montoganado)) + 1    #esto me da a mi un vistaso de cual fue el dia en el que jimena ganado menos dinero 


print(f"Total semanal: ₡{total_semana}")
print(f"Día en que jimena gano menos ganancia: {dias_malos}")     #mostrar el resultado y la ganancia 
