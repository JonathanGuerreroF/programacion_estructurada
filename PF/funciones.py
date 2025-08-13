def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

def menu_usuarios():
    print("\n\t\t..:: 🍔 CHIVATAS BURGUER LOGIN ::..\n")
    print("\t1. Registro")
    print("\t2. Login")
    print("\t3. Salir")
    return input("\n\tSelecciona una opción: ").strip()
