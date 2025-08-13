import conexionBD

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")
    
def mostrar_menu_clientes():
    borrarPantalla()
    print("\n👥=== GESTIÓN DE CLIENTES ===")
    print("1️⃣  📝 Registrar nuevo cliente")
    print("2️⃣  📄 Ver lista de clientes")
    print("3️⃣  🔍 Buscar cliente por nombre")
    print("4️⃣  🗑️ Eliminar cliente")
    print("5️⃣  🔙 Volver al menú principal")

def registrar_cliente():
    borrarPantalla()
    conexion = conexionBD.conectarDB()
    if conexion!=None: 
        print("\n📝 Registro de nuevo cliente")
        nombre = input("👤 Nombre: ").strip()
        telefono = input("📱 Teléfono: ").strip()
        direccion = input("📍 Dirección: ").strip()
        try:
            cursor = conexion.cursor()
            sql = "INSERT INTO clientes (nombre, telefono, direccion) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, telefono, direccion))
            conexion.commit()
            print("✅ Cliente registrado exitosamente")
        except Exception as e:
            print(f"❌ Error al registrar cliente: {e}")
    esperarTecla()

def ver_clientes():
    borrarPantalla()
    conexion = conexionBD.conectarDB()
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT id, nombre, telefono, direccion FROM clientes")
        resultados = cursor.fetchall()

        if not resultados:
            print("📭 No hay clientes registrados.")
        else:
            print("\n📋 Lista de clientes:")
            for i, (id, nombre, telefono, direccion) in enumerate(resultados, 1):
                print(f"{'-'*50}")
                print(f"ID: {id} | {nombre} | Tel: {telefono} | Dirección: {direccion}")
            print(f"{'-'*50}")
    except Exception as e:
        print(f"❌ Error al obtener clientes: {e}")
    
    esperarTecla()

def buscar_cliente():
    borrarPantalla()
    conexion = conexionBD.conectarDB()  
    cursor = conexion.cursor()

    nombre_buscar = input("🔎 Ingresa el nombre del cliente a buscar: ").strip().lower()

    try:
        sql = "SELECT id, nombre, telefono, direccion FROM clientes WHERE LOWER(nombre) LIKE %s"
        cursor.execute(sql, (f"%{nombre_buscar}%",))
        resultados = cursor.fetchall()

        if resultados:
            print("\n🔍 Resultados encontrados:")
            for id, nombre, telefono, direccion in resultados:
                print(f"ID: {id} | {nombre} | Tel: {telefono} | Dirección: {direccion}")
        else:
            print("❌ No se encontró ningún cliente con ese nombre.")
    except Exception as e:
        print(f"❌ Error al buscar cliente: {e}")
    finally:
        cursor.close()
        conexion.close()
    
    esperarTecla()

def eliminar_cliente():
    borrarPantalla()
    ver_clientes()
    try:
        cliente_id = input("🗑️ Ingresa el ID del cliente a eliminar: ").strip()
        conexion = conexionBD.conectarDB()
        cursor = conexion.cursor()
        resp=input(f"¿Deseas eliminar el cliente con ID {cliente_id}? (SI/NO): ").lower().strip()
        sql = "DELETE FROM clientes WHERE id = %s"
        if resp=="si":
            cursor.execute(sql, (cliente_id,))
            if cursor.rowcount == 0:
                print("\n❌ No se encontró el cliente con ese ID.")
            else:
                conexion.commit()
                print("\n🗑️ Cliente eliminado correctamente.")
        else:
            print("\t..::La acción se canceló con éxito::..")

    except Exception as e:
        print(f"❌ Error al eliminar cliente: {e}")
        
    esperarTecla()
    
def menu_clientes():
    opc=True
    while opc:
        mostrar_menu_clientes()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            ver_clientes()
        elif opcion == '3':
            buscar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            print("🔙 Volviendo al menú principal...")
            opc=False
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

# if __name__ == "__clientes__":
#     menu_clientes()














'''
clientes = []

def borrarPantalla():
    import os
    os.system("cls")

def mostrar_menu_clientes():
    borrarPantalla()
    print("\n👥=== GESTIÓN DE CLIENTES ===")
    print("1️⃣  📝 Registrar nuevo cliente")
    print("2️⃣  📄 Ver lista de clientes")
    print("3️⃣  🔍 Buscar cliente por nombre")
    print("4️⃣  🗑️ Eliminar cliente")
    print("5️⃣  🔙 Volver al menú principal")

def registrar_cliente():
    nombre = input("👤 Nombre del cliente: ").strip()
    telefono = input("📱 Teléfono: ").strip()
    historial = input("🛍️ Comentario o historial de compras (opcional): ").strip()

    cliente = {
        "nombre": nombre,
        "telefono": telefono,
        "historial": historial
    }

    clientes.append(cliente)
    print(f"✅ Cliente '{nombre}' registrado correctamente.")

def ver_clientes():
    if not clientes:
        print("📭 No hay clientes registrados.")
    else:
        print("\n📋 Lista de clientes:")
        for i, c in enumerate(clientes, 1):
            print(f"{i}. {c['nombre']} | Tel: {c['telefono']} | Historial: {c['historial']}")

def buscar_cliente():
    nombre_buscar = input("🔎 Ingresa el nombre del cliente a buscar: ").strip().lower()
    encontrados = [c for c in clientes if nombre_buscar in c["nombre"].lower()]
    
    if encontrados:
        print("\n🔍 Resultados encontrados:")
        for c in encontrados:
            print(f"- {c['nombre']} | Tel: {c['telefono']} | Historial: {c['historial']}")
    else:
        print("❌ No se encontró ningún cliente con ese nombre.")

def eliminar_cliente():
    ver_clientes()
    try:
        indice = int(input("🗑️ Ingresa el número del cliente a eliminar: ")) - 1
        if 0 <= indice < len(clientes):
            eliminado = clientes.pop(indice)
            print(f"🗑️ Cliente '{eliminado['nombre']}' eliminado.")
        else:
            print("❌ Número de cliente no válido.")
    except ValueError:
        print("❌ Entrada no válida.")

def menu_clientes():
    while True:
        mostrar_menu_clientes()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            ver_clientes()
        elif opcion == '3':
            buscar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            print("🔙 Volviendo al menú principal...")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

'''