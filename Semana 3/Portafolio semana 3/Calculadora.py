numb1=int(input("ingresa un valor"))
numb2=int(input("ingresa un segundo valor"))

eleccion = 0

while eleccion != 6:
    print("""
    indique la operacion:
          
    1)suma
    2)resta
    3)multiplicacion
    4)division
    5)Volver a realizar otra operacion
    6)salir 
    """)
    
    eleccion=int(input())
    
    if eleccion == 1:
        print(" ")
        print("resultado: ", numb1,"+", numb2, "=",numb1+numb2)
    if eleccion == 2:
        print(" ")
        print("resultado: ", numb1,"-", numb2, "=",numb1-numb2)
    if eleccion == 3:
        print(" ")
        print("resultado: ", numb1,"*", numb2, "=",numb1*numb2)
    if eleccion == 4:
        print(" ")
        print("resultado: ", numb1,"/", numb2, "=",numb1/numb2)
    
    if eleccion== 5:
     numb1=int(input("ingresa un valor"))
     numb2=int(input("ingresa un segundo valor"))