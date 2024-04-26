salarios = []
dinero_adicional = 0
for i in range(15):
    salario = float(input("Ingresa el salario {}: ".format(i+1)))
    salarios.append(salario)
for salario in salarios:
    if salario < 500:
        diferencia = 500 - salario
        dinero_adicional += diferencia
print("Se necesita un total de ${} adicionales para que al menos todos ganen $500.".format(dinero_adicional))
#ejercicio 4