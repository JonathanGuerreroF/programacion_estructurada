#Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar, y consultar peliculas
#-----Notas-----
#1.- Utilizar funciones, mandar llamar desde otro archivo
#2.- Utilizar listas para almacenar los nombres de peliculas
import os
import peliculas as movies
opc=True
while opc:
   os.system("clear")
   print("\n\t..::: CINEPOLIS CLON :::... \n..::: Sistema de Gestión de Peliculas :::...\n 1.- Agregar  \n 2.- Eliminar \n 3.- Actualizar \n 4.- Consultar \n 5.- Buscar \n 6.- Vaciar \n 7.- SALIR ")
   opcion=input("\t Elige una opción: ").upper()
   match opcion:
        case "1":
            movies.borrar_pantalla()
            movies.esperar()
            print(movies.agregar_peliculas())
        case "2":
            movies.borrar_pantalla()
            movies.esperar()
            movies.eliminar_pelicula() 
        case "3":
            movies.borrar_1pantalla()
            movies.esperar()
            movies.modificar_pelicula 
        case "4":
            movies.borrar_pantalla()
            movies.esperar()  
            movies.consultar_pelicula()
        case "5":
            movies.borrar_pantalla()
            movies.esperar()
            movies.buscar_pelicula() 
        case "6":
            os.system("clear") 
            print(".:: Vacias Peliculas ::.") 
            input("Oprima cualquier tecla para continuar ...")
        case "7":
            os.system("clear")
            opcion=False    
            print("Terminaste la ejecucion del SW")
        case _:
            os.system("clear") 
            input("Opción invalida vuelva a intentarlo ... por favor")
            
            
            
