#ENTRADA
tabla = input("Ingrese tabla de multiplicar")
#PROCESO
for contador in range(1,13,1):
    print(tabla + " x " + str(contador) + " = " + str((int(tabla) * contador)))
