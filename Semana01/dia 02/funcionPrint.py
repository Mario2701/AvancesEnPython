"""
print("hola mundo", end = ', ')
print("mi nombre es Mario")
print("=" * 20, end = ' | ')
print(" esto es un titulo ", end = ' | ')
print("=" * 20)
"""
#ENTRADA
lado = int(input("Ingrese el lado del cuadrado: "))
#PROCESO
for contador in range (1,lado + 1,1):
    if(contador == 1 or contador == lado):
        print("* " * lado)
    else:
        print('*' + str('  ' * (lado - 2)) + ' *')


