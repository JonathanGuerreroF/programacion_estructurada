import funciones  
from usuarios import usuario
import getpass

# Aquí importas tus menús reales si login tiene éxito
from inventario import inventario
from clientes import clientes
from proveedores import proveedores
import reportes.reportes as reportes

def menu_sistema(usuario):
    opcion = True
    while opcion:
        funciones.borrarPantalla()
        print(f"\n\t🎉 Bienvenido/a {usuario[1]} {usuario[2]} a CHIVATAS BURGUER 🎉\n")
        print("\t1. Gestión de Inventario 📦")
        print("\t2. Gestión de Clientes 👥")
        print("\t3. Gestión de Proveedores 🚚")
        print("\t4. Reportes 📊")
        print("\t5. Cerrar sesión 🔒")

        eleccion = input("\n\tSelecciona una opción: ").strip()

        if eleccion == "1":
            inventario.menu_inventario()
        elif eleccion == "2":
            clientes.menu_clientes()
        elif eleccion == "3":
            proveedores.menu_proveedores()
        elif eleccion == "4":
            reportes.menu_reportes()
        elif eleccion == "5":
            print("\n🔒 Sesión finalizada. Volviendo al login...")
            opcion = False
        else:
            print("❌ Opción no válida.")
            funciones.esperarTecla()

def main():
    continuar = True
    while continuar:
        funciones.borrarPantalla()
        opcion = funciones.menu_usuarios()

        if opcion == "1" or opcion.upper() == "REGISTRO":
            funciones.borrarPantalla()
            print("\n\t..:: Registro de Usuario ::..")
            nombre = input("\tNombre: ").upper().strip()
            apellidos = input("\tApellidos: ").upper().strip()
            email = input("\tCorreo electrónico: ").lower().strip()
            password = getpass.getpass("\tContraseña: ").strip()
            resultado = usuario.registrar(nombre, apellidos, email, password)
            if resultado:
                print(f"\n✅ {nombre} {apellidos} registrado con éxito.")
            else:
                print("\n❌ No se pudo registrar. Intenta de nuevo.")
            funciones.esperarTecla()

        elif opcion == "2" or opcion.upper() == "LOGIN":
            funciones.borrarPantalla()
            print("\n\t..:: Inicio de Sesión ::..")
            email = input("\tCorreo electrónico: ").lower().strip()
            password = getpass.getpass("\tContraseña: ").strip()
            registro = usuario.iniciar_sesion(email, password)
            if registro:
                menu_sistema(registro)
            else:
                print("\n❌ Email y/o contraseña incorrectos.")
                funciones.esperarTecla()

        elif opcion == "3" or opcion.upper() == "SALIR":
            print("\n👋 Gracias por usar el sistema. ¡Hasta luego!")
            continuar = False
        else:
            print("\n❌ Opción inválida.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()





'''
import clientes.clientes
import inventario
import clientes
import inventario.inventario
import proveedores
import proveedores.proveedores
import reportes

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

opcion = True
while opcion:
    borrarPantalla()
    print("\n\t\t\t..::: 🍔 CHIVATAS BURGUER :::...\n\t\t..::: Sistema Administrativo :::...\n")
    print("\t\t 1.- Inventario 📦")
    print("\t\t 2.- Clientes 👥")
    print("\t\t 3.- Proveedores 🚚")
    print("\t\t 4.- Reportes 📊")
    print("\t\t 5.- Salir 🚪")
    
    entrada = input("\n\t\tElige una opción: ").upper()

    match entrada:
        case "1":
            inventario.inventario.menu_inventario()
            esperarTecla()
        case "2":
            clientes.clientes.menu_clientes()
            esperarTecla()
        case "3":
            proveedores.proveedores.menu_proveedores()
            esperarTecla()
        case "4":
            reportes.menu_reportes()
            esperarTecla()
        case "5":
            opcion = False
            borrarPantalla()
            print("\n\t👋 Terminaste la ejecución del sistema. ¡Hasta pronto!")
        case _:
            input("\n❌ Opción inválida, vuelve a intentarlo...")


'''






'''
def borrarPantalla():
    import os
    os.system("cls")

def mostrar_menu():
    borrarPantalla()
    print("\n🍔=== SISTEMA ADMINISTRATIVO: CHIVATAS BURGUER ===🍟")
    print("1️⃣  📦 Gestión de Inventario")
    print("2️⃣  👥 Gestión de Clientes")
    print("3️⃣  🚚 Gestión de Proveedores")
    print("4️⃣  📊 Reportes")
    print("5️⃣  ❌ Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == '1':
            try:
                import inventario
                inventario.menu_inventario()
            except ModuleNotFoundError:
                print("⚠️  Módulo de inventario no disponible aún.")
        elif opcion == '2':
            try:
                import clientes
                clientes.menu_clientes()
            except ModuleNotFoundError:
                print("⚠️  Módulo de clientes no disponible aún.")
        elif opcion == '3':
            try:
                import proveedores
                proveedores.menu_proveedores()
            except ModuleNotFoundError:
                print("⚠️  Módulo de proveedores no disponible aún.")
        elif opcion == '4':
            try:
                import reportes
                reportes.menu_reportes()
            except ModuleNotFoundError:
                print("⚠️  Módulo de reportes no disponible aún.")
        elif opcion == '5':
            print("👋 Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()

'''