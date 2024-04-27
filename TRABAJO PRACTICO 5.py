"""1) Hacer un programa que gestiones datos para una escuela.
El programa tiene que ser capaz de:
a) Llevar un registro de todos los datos de alumnos de la escuela 
(Nombre, Apellido, fecha de nacimiento, DNI, Nombre de Tutor,
registro de todas las notas, cantidad de faltas, cantidad de amonestaciones recibidas."""


print (F"BIENVENIDOS AL AULA 'A' DEL INSTITUTO IITA, ESTE ES SU MENU DE OPCIONES: ")

lista_de_alumnos = ["Francisco", "Federico", "Marina"]

datos_de_Aumnos = {
    
"Francisco":{"nombre":"Francisco",
"apellido": "Flores",
 "DNI": 35194399,
 "fecha de nacimiento":"23/06/1990",
 "Tutor":"Santiago Flores",
 "notas": [10,7,8,6,9],
 "faltas": 2,
 "amonestaciones": 0},
    
"Federico":{"nombre":"Federico",
"apellido": "Rocha",
 "DNI": 36856321,
 "fecha de nacimiento":"09/04/1992",
 "Tutor":"Facundo Rocha",
 "notas": [8,9,7,5,10],
 "faltas": 6,
 "amonestaciones": 2},

"Marina":{"nombre":"Marina",
"apellido": "Gareca",
 "DNI": 37720727,
 "fecha de nacimiento":"08/09/1993",
 "Tutor":"Pablo Gareca de la Cruz",
 "notas": [9,9,8,9,10],
 "faltas": 0,
 "amonestaciones": 0}} 


def opcion1():
    print(f"El listado de alumnos del aula (A) es: {lista_de_alumnos}")

def opcion2():
    print("Elija un numero de opción: ")
    
    def eleccion1():
        print(datos_de_Aumnos["Francisco"])
    def eleccion2():
        print(datos_de_Aumnos["Federico"])
    def eleccion3():
        print(datos_de_Aumnos["Marina"])
    
    def mostrar_sub_menu():
        print("Opción 1. datos de Francisco" )
        print ("Opción 2. datos de Federico")
        print("Opción 3.datos de Marina")
    
    def menu2():
       
            mostrar_sub_menu()
            opcion2 = input("Seleccione una opcion: ")
            if opcion2 == "1":
                eleccion1()
            elif opcion2 == "2":
                eleccion2()
            elif opcion2 == "3":
                eleccion3()
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
                
    menu2()
  

def opcion3():
    print("Quite a un alumno del listado")

    
    def eleccion4():
        print(f"Los alumnos que quedaron son: {lista_de_alumnos[1]}, {lista_de_alumnos[2]}")
    def eleccion5():
        print(f"Los alumnos que quedaron son: {lista_de_alumnos[0]}, {lista_de_alumnos[2]}")
    def eleccion6():
        print(f"Los alumnos que quedaron son: {lista_de_alumnos[0]}, {lista_de_alumnos[1]}")
    
    def mostrar_sub_menu3():
        print("Opción 1. Francisco" )
        print ("Opción 2. Federico")
        print("Opción 3. Marina")
    
    def menu3():
       
            mostrar_sub_menu3()
            opcion3 = input("Seleccione una opcion: ")
            if opcion3 == "1":
                eleccion4()
            elif opcion3 == "2":
                eleccion5()
            elif opcion3 == "3":
                eleccion6()
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
    
    menu3()
        
    
def opcion4():
    print ("Agregue un estudiante a la lista del aula (A)")
    nuevo_estudiante = input(f"Escriba el nombre del estudiante: ")
    lista_de_alumnos.append(nuevo_estudiante)
    print ("La lista actualizada de estudientes es: ",lista_de_alumnos)
   
    
def mostrar_menu():
    print("Menú de opciones:")
    print("1. Opción 1, lista de alumnos")
    print("2. Opción 2, Mostrar los datos de cada alumno")
    print("3. Opción 3, Expulsar Alumnos")
    print("4. Opción 4, Agregar Alumnos")
    print("5. Salir") 

def menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            opcion4()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()

