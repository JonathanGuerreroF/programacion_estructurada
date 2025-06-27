import peliculasDago

opcion=True
while opcion:
    peliculasDago.borrarPantalla()
    print("\n\t\t\t..::: CINEPOLIS CLON :::... \n\t\t..::: Sistema de Gestión de Peliculas :::...\n\t\t 1.- Agregar  \n\t\t 2.- Eliminar \n\t\t 3.- Actualizar \n\t\t 4.- Consultar \n\t\t 5.- Buscar \n\t\t 6.- Vaciar \n\t\t 7.- SALIR ")
    opcion=input("\n\t\tElige una opción: ").upper()

    match opcion:
        case "1":
            peliculasDago.agregarPeliculas()
            peliculasDago.esperarTecla()
        case "2":
            peliculasDago.eliminarPeliculas()
            peliculasDago.esperarTecla()
        case "3":
            peliculasDago.modificarPelicula()
            peliculasDago.esperarTecla()
        case "4":
            peliculasDago.consultarPeliculas()
            peliculasDago.esperarTecla()
        case "5": 
            peliculasDago.buscarPeliculas()
            peliculasDago.esperarTecla()
        case "6":
             peliculasDago.vaciarPeliculas()
             peliculasDago.esperarTecla()
        case "7":
            opcion=False    
            peliculasDago.borrarPantalla()
            print("\n\tTerminaste la ejecucion del SW")
        case _: 
            input("\n\tOpción invalida vuelva a intentarlo ... por favor")