def convertir_a_binario(numero):
    resultado = bin(numero)
    print(f"Número {numero} en binario: {resultado}")

def convertir_a_octal(numero):
    resultado = oct(numero)
    return resultado

def convertir_a_hexadecimal(numero):
    resultado = hex(numero)
    return resultado

def mostrar_valor_en_base(numero, base):
    if base == 2:
        convertir_a_binario(numero)
    elif base == 8:
        resultado_octal = convertir_a_octal(numero)
        print(f"Número {numero} en octal: {resultado_octal}")
    elif base == 16:
        resultado_hexadecimal = convertir_a_hexadecimal(numero)
        print(f"Número {numero} en hexadecimal: {resultado_hexadecimal}")
    else:
        print("Base no válida. Introduce 2 para binario, 8 para octal o 16 para hexadecimal.")

# Programa principal
numero = int(input("Ingrese un número entero: "))

mostrar_valor_en_base(numero, 2)
mostrar_valor_en_base(numero, 8)
mostrar_valor_en_base(numero, 16)
