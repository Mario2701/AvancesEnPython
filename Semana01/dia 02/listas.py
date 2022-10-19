dia = "Lunes"
dia2 = "Martes"
#Creando una lista(se crea entre corchetes)
dias = ["Lunes","Martes","Miercoles"]

dias.append("Jueves") #agrega un nuevo valor
#dias.pop() #le quita el ultimo valor de la lista
dias.pop(3) #le quita el 3 valor de la lista
print(dias)

#actualizar un valor
dias[0] = "Domingo"
print(dias)

#recorrer una lista
for mostrarDias in dias:
    print(mostrarDias)