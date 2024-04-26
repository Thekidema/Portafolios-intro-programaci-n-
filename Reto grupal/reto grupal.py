def agregar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "a") as archivo:
            nombre_vendedor = input("Ingrese el nombre del vendedor: ")
            monto_venta = float(input("Ingrese el monto de la venta en dólares: "))
            archivo.write(f"{nombre_vendedor}: {monto_venta}\n")
        print("Datos agregados correctamente al archivo.")
    except FileNotFoundError:
        print("No se encontró el archivo.")

def mostrar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            print("Datos de ventas:")
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("No se encontró el archivo.")

if __name__ == "__main__":
    nombre_archivo = "ventas.txt"

    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar datos de ventas")
        print("2. Mostrar datos de ventas")
        print("3. Salir")
        opcion = input("Ingrese el número de la opción: ")

        if opcion == "1":
            agregar_datos(nombre_archivo)
        elif opcion == "2":
            mostrar_datos(nombre_archivo)
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Por favor, ingrese un número válido.")
#PARTIPANTES EMANUEL CV, Erick Portocarrero