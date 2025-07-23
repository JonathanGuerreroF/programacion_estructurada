def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t\t ... Oprima cualquier tecla ...")

def menuPrincipal():
    print('.:: Sistema de gestion de notas ::. \n1.- Registro  \n2.- Login \n3.- Salir ')
    opcion = input('Elige una opcion').upper()
    return opcion