import os
import time
"""
CRUD 
C = CREATE
R = READ
U = UPDATE
D = DELETE
"""
#funciona un CLS

alumno = {
    'nombre': 'Mario Grande',
    'email': '77269474@continental.edu.pe',
    'celular': '921473096'
}

listaAlumnos = [alumno]
print(listaAlumnos)

op = 0
while (op != "5"):
    if(op != "0"):
        time.sleep(2)
        os.system("cls")
    print(
        """
        =================================================
         PROGRAMA DE MATRICULA A DE LOS ALUMNOS DE CODIGO
        =================================================
        [1] REGISTRAR ALUMNO
        [2] MOSTRAR ALUMNOS
        [3] ACTUALIZAR ALUMNO
        [4] ELIMINAR ALUMNO
        [5] SALIR DEL PROGRAMA
        """
    )
    op = input("Ingrese la opcion: ")
    if (op == "1"):
        print("[1] REGISTRAR ALUMNO")
        nombre = input("Nombre: ")
        email = input("Email: ")
        celular = input("Celular: ")
        dicNuevoAlumno = {
            'nombre': nombre,
            'email': email,
            'celular': celular
        }
        listaAlumnos.append(dicNuevoAlumno)
        print("ALUMNO REGISTRADO CON EXITO")
        
        
        
        
    elif (op == "2"):
        print("[2] MOSTRAR ALUMNO")
        
        for alumno in listaAlumnos:
            print("-" * 20)
            for a,b in alumno.items(): #items es una funcion
                print(a + " : " + b)
        
        
                
    elif (op == "3"):
        print("[3] ACTUALIZAR ALUMNO")
        #PASO 1: buscar por el email el diccionario a editar
        valorBusqueda = input('Ingrese el email del alumno a actualizar: ')
        for contador in range(len(listaAlumnos)):
            dicAlumno = listaAlumnos[contador]
            for a,b in dicAlumno.items():
                if(a == 'email' and b == valorBusqueda):
                    posicionBusqueda = contador
                    break
                
        if(posicionBusqueda == -1):
            print('ALUMNO NO ENCONTRADO')
        else:
            print("ALUMNO ENCONTRADO : " + listaAlumnos[posicionBusqueda].get("nombre"))
            print("INGRESE NUEVOS VALORES PARA EL ALUMNO ENCONTRADO")
            
            nombre = input('NUEVO NOMBRE : ')
            if(nombre == ''):
                nombre = listaAlumnos[posicionBusqueda].get("nombre")
                
            email = input('NUEVO EMAIL : ')
            if(email == ''):
                email = listaAlumnos[posicionBusqueda].get('email')
                
            celular = input('NUEVO CELULAR : ')
            if(celular == ''):
                celular = listaAlumnos[posicionBusqueda].get('celular')
                
            dicAlumnoEditar = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }
            #actualizamos el diccionario en la lista
            listaAlumnos[posicionBusqueda] = dicAlumnoEditar
            print('ALUMNO ACTUALIZADO !!!')
    elif (op == "4"):
        print("[4] ELIMINAR ALUMNO")
        
    elif (op == "5"):
        print("[5] ESTA SALIENDO DEL PROGRAMA...")
    else:
        print(" OPCION NO VALIDA !!!")
