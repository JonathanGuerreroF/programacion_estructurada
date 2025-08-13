import conexionBD

def borrarPantalla():
    import os
    os.system("cls" if os.name == "nt" else "clear")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

def mostrar_menu_proveedores():
    borrarPantalla()
    print("\n🚚=== GESTIÓN DE PROVEEDORES ===")
    print("1️⃣  📝 Registrar nuevo proveedor")
    print("2️⃣  📄 Ver lista de proveedores")
    print("3️⃣  🔍 Buscar proveedor por nombre")
    print("4️⃣  🗑️ Eliminar proveedor")
    print("5️⃣  🔙 Volver al menú principal")

def registrar_proveedor():
    borrarPantalla()
    conexion = conexionBD.conectarDB()
    if conexion is not None:
        print("\n📝 Registro de nuevo proveedor")
        nombre = input("🏷️ Nombre del proveedor: ").strip()
        contacto = input("📦 Productos que provee: ").strip()
        telefono = input("📱 Teléfono: ").strip()
        direccion = input("📍 Dirección: ").strip()

        try:
            cursor = conexion.cursor()
            sql = """
                INSERT INTO proveedores (nombre, contacto, telefono, direccion)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (nombre, contacto, telefono, direccion))
            conexion.commit()
            print("✅ Proveedor registrado exitosamente")
        except Exception as e:
            print(f"❌ Error al registrar proveedor: {e}")

    esperarTecla()

def ver_proveedores():
    borrarPantalla()
    conexion = conexionBD.conectarDB()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT id, nombre, contacto, telefono, direccion FROM proveedores")
        resultados = cursor.fetchall()

        if not resultados:
            print("📭 No hay proveedores registrados.")
        else:
            print("\n📋 Lista de proveedores:")
            for i, (id, nombre, contacto, telefono, direccion) in enumerate(resultados, 1):
                print(f"{'-'*80}")
                print(f"ID: {id} | {nombre} | Productos: {contacto} | Tel: {telefono} | Dir: {direccion}")
            print(f"{'-'*80}")
    except Exception as e:
        print(f"❌ Error al obtener proveedores: {e}")

    esperarTecla()

def buscar_proveedor():
    borrarPantalla()
    conexion = conexionBD.conectarDB()
    cursor = conexion.cursor()

    nombre_buscar = input("🔎 Ingresa el nombre del proveedor a buscar: ").strip().lower()

    try:
        sql = "SELECT id, nombre, contacto, telefono, direccion FROM proveedores WHERE LOWER(nombre) LIKE %s"
        cursor.execute(sql, (f"%{nombre_buscar}%",))
        resultados = cursor.fetchall()

        if resultados:
            print("\n🔍 Resultados encontrados:")
            for id, nombre, contacto, telefono, direccion in resultados:
                print(f"{'-'*80}")
                print(f"ID: {id} | {nombre} | Productos: {contacto} | Tel: {telefono} | Dir: {direccion}")
            print(f"{'-'*80}")
        else:
            print("❌ No se encontró ningún proveedor con ese nombre.")
    except Exception as e:
        print(f"❌ Error al buscar proveedor: {e}")
    finally:
        cursor.close()
        conexion.close()

    esperarTecla()

def eliminar_proveedor():
    borrarPantalla()
    ver_proveedores()
    try:
        proveedor_id = input("🗑️ Ingresa el ID del proveedor a eliminar: ").strip()
        resp = input(f"¿Deseas eliminar el proveedor con ID {proveedor_id}? (SI/NO): ").lower().strip()
        
        if resp == "si":
            conexion = conexionBD.conectarDB()
            cursor = conexion.cursor()
            sql = "DELETE FROM proveedores WHERE id = %s"
            cursor.execute(sql, (proveedor_id,))
            if cursor.rowcount == 0:
                print("❌ No se encontró el proveedor con ese ID.")
            else:
                conexion.commit()
                print("🗑️ Proveedor eliminado correctamente.")
        else:
            print("\t..:: La acción se canceló con éxito ::..")
    except Exception as e:
        print(f"❌ Error al eliminar proveedor: {e}")

    esperarTecla()

def menu_proveedores():
    opc = True
    while opc:
        mostrar_menu_proveedores()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == '1':
            registrar_proveedor()
        elif opcion == '2':
            ver_proveedores()
        elif opcion == '3':
            buscar_proveedor()
        elif opcion == '4':
            eliminar_proveedor()
        elif opcion == '5':
            print("🔙 Volviendo al menú principal...")
            opc = False
        else:
            input("❌ Opción no válida. Intenta nuevamente.")


























'''
proveedores = []

def borrarPantalla():
    import os
    os.system("cls")

def mostrar_menu_proveedores():
    borrarPantalla()
    print("\n🚚=== GESTIÓN DE PROVEEDORES ===")
    print("1️⃣  📝 Registrar nuevo proveedor")
    print("2️⃣  📄 Ver lista de proveedores")
    print("3️⃣  🔍 Buscar proveedor por nombre")
    print("4️⃣  🗑️ Eliminar proveedor")
    print("5️⃣  🔙 Volver al menú principal")

def registrar_proveedor():
    nombre = input("🏷️ Nombre del proveedor: ").strip()
    productos = input("📦 Productos que provee: ").strip()
    telefono = input("📱 Teléfono: ").strip()
    direccion = input("📍 Dirección (opcional): ").strip()

    proveedor = {
        "nombre": nombre,
        "productos": productos,
        "telefono": telefono,
        "direccion": direccion
    }

    proveedores.append(proveedor)
    print(f"✅ Proveedor '{nombre}' registrado correctamente.")

def ver_proveedores():
    if not proveedores:
        print("📭 No hay proveedores registrados.")
    else:
        print("\n📋 Lista de proveedores:")
        for i, p in enumerate(proveedores, 1):
            print(f"{i}. {p['nombre']} | Productos: {p['productos']} | Tel: {p['telefono']} | Dir: {p['direccion']}")

def buscar_proveedor():
    nombre_buscar = input("🔎 Ingresa el nombre del proveedor a buscar: ").strip().lower()
    encontrados = [p for p in proveedores if nombre_buscar in p["nombre"].lower()]
    
    if encontrados:
        print("\n🔍 Resultados encontrados:")
        for p in encontrados:
            print(f"- {p['nombre']} | Productos: {p['productos']} | Tel: {p['telefono']} | Dir: {p['direccion']}")
    else:
        print("❌ No se encontró ningún proveedor con ese nombre.")

def eliminar_proveedor():
    ver_proveedores()
    try:
        indice = int(input("🗑️ Ingresa el número del proveedor a eliminar: ")) - 1
        if 0 <= indice < len(proveedores):
            eliminado = proveedores.pop(indice)
            print(f"🗑️ Proveedor '{eliminado['nombre']}' eliminado.")
        else:
            print("❌ Número de proveedor no válido.")
    except ValueError:
        print("❌ Entrada no válida.")

def menu_proveedores():
    while True:
        mostrar_menu_proveedores()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == '1':
            registrar_proveedor()
        elif opcion == '2':
            ver_proveedores()
        elif opcion == '3':
            buscar_proveedor()
        elif opcion == '4':
            eliminar_proveedor()
        elif opcion == '5':
            print("🔙 Volviendo al menú principal...")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")
'''