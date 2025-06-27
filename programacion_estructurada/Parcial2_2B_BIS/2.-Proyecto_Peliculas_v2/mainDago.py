#Notas
# 1.- Utilizar funciones y mandar a llamar desde otro archivo
# 2.-Utilizar dict para almacenar los siguientes atributos: nombre, categoria, clasificacion, genero, idioma de las peliculas

import peliculasDago

opcion=True
while opcion:
    peliculasDago.borrarPantalla()
    print("\n\t\t\t..::: \U0001F3AC CINEPOLIS CLON :::...\n\t\t..::: Sistema de Gestión de Películas :::...\n")
    print("\t\t 1.- Crear \U0001F4DD\n\t\t 2.- Borrar \U0001F4DB\n\t\t 3.- Mostrar \U0001F50D\n\t\t 4.- Agregar Características \U0001F4BE\n\t\t 5.- Modificar Características \U0001F501\n\t\t 6.- Borrar Características \U0001F4DB\n\t\t 7.- SALIR \U0001F6AA")
    opcion=input("\n\t\tElige una opción: ").upper()

    match opcion:
        case "1":
            peliculasDago.crearPeliculas()
            peliculasDago.esperarTecla()
        case "2":
            peliculasDago.borrarPeliculas()
            peliculasDago.esperarTecla()
        case "3":
            peliculasDago.mostrarPeliculas()
            peliculasDago.esperarTecla()
        case "4":
            peliculasDago.agregarCaracteristicaPeliculas()
            peliculasDago.esperarTecla()
        case "5": 
            peliculasDago.modificarCaracteristicaPeliculas()
            peliculasDago.esperarTecla()
        case "6":
             peliculasDago.borrarCaracteristicasPeliculas()
             peliculasDago.esperarTecla()
        case "7":
            opcion=False    
            peliculasDago.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")