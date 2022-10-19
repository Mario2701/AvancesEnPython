#Las tuplas no se pueden eliminar ()
dias = ("Lunes","Martes","Miercoles")

print(dias)
dias = list(dias)
dias.append("Jueves")
print(dias)

dias = tuple(dias)

for totalDias in dias:
    print(totalDias)
