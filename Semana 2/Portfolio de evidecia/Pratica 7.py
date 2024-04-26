sumar_edades= 0
for i in range(5):
    while True:
        try:
            edad=int(input(f"ingrese un valor entero{i+1}: "))
            sumar_edades+=edad
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
promedio=sumar_edades/5
print(f"La edad promedio de las 5 personas es: {promedio}")
