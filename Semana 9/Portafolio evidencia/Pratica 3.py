#Se requiere un programa que imprima una palabra al revés, debe 
#funcionar para cualquier palabra, por lo cual debe utilizar instrucciones 
#de lectura. En la solución utilice ciclos
palabra = input("Ingrese una palabra: ")    #pedir que palabra desea agregar el usuario 


palabra_al_reves = ""  #crear una cadena vacia para que la palabra se pueda impirmir al reves

# Recorrer la palabra de atrás hacia adelante utilizando un bucle
for i in range(len(palabra) - 1, -1, -1):     #hacer que la palabra  se invierta  utilizando los ciclos 
    palabra_al_reves += palabra[i]


print("Palabra inversa:", palabra_al_reves)
