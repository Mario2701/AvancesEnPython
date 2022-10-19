#Las cadenas son matrices
from traceback import print_list


x = "Mi nombre de Jarod"

print(x[3])
print(x[3:8]) #llega hasta el octavo caracter y 1 menos

#BUCLE A TRAVES DE UNA CADENA
for y in "banana":
    print(y)

for z in "Negro de color":
    print(z)
    
#LONGITUD DE CUERDA
a = "Python is awesome"
print(len(a))

b = "Python is the program perfect"
print(len(b))

#COMPROBAR CADENA
txt = "The best things in life are free!"
print("best" in txt)

txt1 = "of course men and you"
print("course" in txt1)

txt3 = "Pero que monada"
if("que" in txt3):
    print("El caracter que se ha encontrado")
    
#Marque si NO

txt1 = "of course men and you"
print("tamos" not in txt1)

txt = "The best things in life are free!"
print("bien" not in txt)
