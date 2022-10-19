# PROGRMA PARA CONVERTIR MONEDAS POR EL TIPO DE CAMBIO
# SOLES A DOLES Y VICEVERSA

# ENTRADA
from ast import Pass


opcion = 0

while (opcion != 3):
    print("""
      ======================================
      CONVERTIDOR DE MONEDAS VERSION 1.0
      ======================================
      OPCION 1: Convertir de soles a dolares
      OPCION 2: Convertir de dolares a soles
      OPCION 3: Salir
      """)
    opcion = int(input("Ingrese una opcion segun el menu: "))
    # PROCESO
    if (opcion == 1):
        # CONVERTIR DE SOLES A DOLARES
        montoOrigen = float(input("Ingrese el monto en soles: "))
        montoDestino = montoOrigen / 3.977
        monedaDestino = "dolares"

    elif (opcion == 2):
        montoOrigen = float(input("Ingrese el monto en dolares: "))
        montoDestino = montoOrigen * 3.977
        monedaDestino = "soles"
        
    elif (opcion == 3):
        print("Gracias por usar la conversion de monedas")

    else:
        print("debe ingresar una opcion valida...")

    # SALIDA
    if(opcion == 1 or opcion == 2):
        print("El monto en " + monedaDestino + " es " + str(montoDestino))
