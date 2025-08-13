import conexionBD

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

def mostrar_menu_inventario():
    borrarPantalla()
    print("\n📦=== GESTIÓN DE INVENTARIO ===")
    print("1️⃣  ➕ Agregar producto")
    print("2️⃣  📋 Ver inventario")
    print("3️⃣  📝 Actualizar stock")
    print("4️⃣  🗑️ Eliminar producto")
    print("5️⃣  🔙 Volver al menú principal")

def agregar_producto():
    borrarPantalla()
    conexion = conexionBD.conectarDB()
    if conexion != None:
        print("\n🆕 Agregar nuevo producto")
        nombre = input("🔤 Nombre del producto: ").strip()
        cantidad = input("🔢 Cantidad: ").strip()
        unidad = input("📏 Unidad (ej. kg, piezas, litros): ").strip()
        precio = input("💲 Precio unitario: ").strip()
        descripcion = input("📝 Descripción (opcional): ").strip()
        proveedor_id = input("🔗 ID del proveedor (opcional): ").strip()

        proveedor_id = int(proveedor_id) if proveedor_id else None

        try:
            cursor = conexion.cursor()
            sql = """
                INSERT INTO productos (nombre, cantidad, unidad, precio, descripcion, proveedor_id)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            datos = (nombre, cantidad, unidad, precio, descripcion, proveedor_id)
            cursor.execute(sql, datos)
            conexion.commit()
            print("✅ Producto agregado exitosamente")
        except Exception as e:
            print(f"❌ Error al agregar producto: {e}")
    
    esperarTecla()

def ver_inventario():
    borrarPantalla()
    conexion = conexionBD.conectarDB()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            SELECT p.id, p.nombre, p.cantidad, p.unidad, p.precio, pr.nombre AS proveedor
            FROM productos p
            LEFT JOIN proveedores pr ON p.proveedor_id = pr.id
        """)
        resultados = cursor.fetchall()

        if not resultados:
            print("📭 El inventario está vacío.")
        else:
            print("\n📋 Inventario actual:")
            for i, (id, nombre, cantidad, unidad, precio, proveedor) in enumerate(resultados, 1):
                print(f"ID: {id} | {nombre} - {cantidad} {unidad} - ${precio:.2f} | Proveedor: {proveedor or 'N/A'}")
    except Exception as e:
        print(f"❌ Error al mostrar inventario: {e}")
    
    esperarTecla()

def actualizar_stock():
    borrarPantalla()
    ver_inventario()
    try:
        producto_id = int(input("\n✏️ Ingresa el ID del producto a actualizar: "))
        nueva_cantidad = input("🔄 Nueva cantidad: ").strip()

        conexion = conexionBD.conectarDB()
        cursor = conexion.cursor()
        sql = "UPDATE productos SET cantidad = %s WHERE id = %s"
        cursor.execute(sql, (nueva_cantidad, producto_id))
        if cursor.rowcount == 0:
            print("❌ No se encontró el producto con ese ID.")
        else:
            conexion.commit()
            print("✅ Stock actualizado correctamente.")
    except Exception as e:
        print(f"❌ Error al actualizar producto: {e}")
    
    esperarTecla()

def eliminar_producto():
    borrarPantalla()
    ver_inventario()
    try:
        producto_id = input("🗑️ Ingresa el ID del producto a eliminar: ").strip()
        resp = input(f"¿Deseas eliminar el producto con ID {producto_id}? (SI/NO): ").lower().strip()
        
        if resp == "si":
            conexion = conexionBD.conectarDB()
            cursor = conexion.cursor()
            sql = "DELETE FROM productos WHERE id = %s"
            cursor.execute(sql, (producto_id,))
            if cursor.rowcount == 0:
                print("❌ No se encontró el producto con ese ID.")
            else:
                conexion.commit()
                print("🗑️ Producto eliminado correctamente.")
        else:
            print("\t..:: La acción se canceló con éxito ::..")
    except Exception as e:
        print(f"❌ Error al eliminar producto: {e}")

    esperarTecla()


def menu_inventario():
    opc = True
    while opc:
        mostrar_menu_inventario()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            ver_inventario()
        elif opcion == '3':
            actualizar_stock()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("🔙 Volviendo al menú principal...")
            opc = False
        else:
            input("❌ Opción no válida. Intenta nuevamente.")































'''
inventario = []

def borrarPantalla():
    import os
    os.system("cls")

def mostrar_menu_inventario():
    borrarPantalla()
    print("\n📦=== GESTIÓN DE INVENTARIO ===")
    print("1️⃣  ➕ Agregar producto")
    print("2️⃣  📋 Ver inventario")
    print("3️⃣  📝 Actualizar stock")
    print("4️⃣  🗑️ Eliminar producto")
    print("5️⃣  🔙 Volver al menú principal")

def agregar_producto():
    nombre = input("🆕 Nombre del producto: ").strip()
    cantidad = input("🔢 Cantidad: ").strip()
    unidad = input("📏 Unidad (ej. kg, piezas, litros): ").strip()
    producto = {
        "nombre": nombre,
        "cantidad": cantidad,
        "unidad": unidad
    }
    inventario.append(producto)
    print(f"✅ Producto '{nombre}' agregado correctamente.")

def ver_inventario():
    if not inventario:
        print("📭 El inventario está vacío.")
    else:
        print("\n📋 Inventario actual:")
        for i, producto in enumerate(inventario, start=1):
            print(f"{i}. {producto['nombre']} - {producto['cantidad']} {producto['unidad']}")

def actualizar_stock():
    ver_inventario()
    try:
        indice = int(input("✏️ Ingresa el número del producto a actualizar: ")) - 1
        if 0 <= indice < len(inventario):
            nueva_cantidad = input("🔄 Nueva cantidad: ").strip()
            inventario[indice]['cantidad'] = nueva_cantidad
            print("✅ Cantidad actualizada correctamente.")
        else:
            print("❌ Número de producto no válido.")
    except ValueError:
        print("❌ Entrada no válida.")

def eliminar_producto():
    ver_inventario()
    try:
        indice = int(input("🗑️ Ingresa el número del producto a eliminar: ")) - 1
        if 0 <= indice < len(inventario):
            eliminado = inventario.pop(indice)
            print(f"🗑️ Producto '{eliminado['nombre']}' eliminado.")
        else:
            print("❌ Número de producto no válido.")
    except ValueError:
        print("❌ Entrada no válida.")

def menu_inventario():
    while True:
        mostrar_menu_inventario()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            ver_inventario()
        elif opcion == '3':
            actualizar_stock()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("🔙 Volviendo al menú principal...")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

'''