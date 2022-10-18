#manejo de variables en python
#suma de dos numeros
#DATOS DE ENTRADA
from turtle import clear

moneda = "soles"
montoSoles = input("Ingrese el monto en soles: ")
#PROCESO
montoDolares = float(montoSoles) / 3.977
#DATOS DE SALIDA
print("El monto en soles es: " + str(montoDolares))