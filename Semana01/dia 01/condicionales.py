#ENTRADA
numero1 = input("Numero 1: ")
numero2 = input("Numero 2: ")
operacion = input("Operacion a ejecutar: ")
#PROCESO
if(operacion == "+"):
    resultado = int(numero1) + int(numero2)
elif(operacion == "-"):
    resultado = int(numero1) - int(numero2)
else:
    resultado = "nn"
#SALIDA
if(resultado == "nn"):
    print("EL operador ingresado es incorrecto")
else:
    print("El resultado es " + str(resultado))
print("Adios!!!")