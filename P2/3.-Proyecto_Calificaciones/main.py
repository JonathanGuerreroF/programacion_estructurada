#Proyecto 3
# Crear un proyecto que permita gestionar calificaciones. Colocar menu de opciones para agregar, mostrar, calcular promedio, calificaciones de un estudiante

#Notas
# 1.- Utilizar funciones y mandar a llamar desde otro archivo (modulos)


import calificaciones

def main():
    datos=[]
    opcion=True

    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menuPrincipal()
        match opcion:
            case "1":
                calificaciones.agregarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrarCalificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.promedios(datos)
                calificaciones.esperarTecla()
            case "4":
                calificaciones.buscarCalificacion(datos)
                calificaciones.esperarTecla()
            case "5":
                opcion=False    
                calificaciones.borrarPantalla()
                print("\n\t \U0001F389 Terminaste la ejecucion del SW \U0001F389 ")
            case _: 
                input("\n\t \U0001F501 Opción invalida vuelva a intentarlo ... por favor")
                
if __name__=="__main__":
    main()