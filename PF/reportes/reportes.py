from conexionBD import conectarDB
import pandas as pd
from datetime import datetime
import os

def borrarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu_reportes():
    borrarPantalla()
    print("\n📊=== REPORTES DEL SISTEMA ===")
    print("1️⃣  📦 Reporte de Inventario")
    print("2️⃣  👥 Reporte de Clientes")
    print("3️⃣  🚚 Reporte de Proveedores")
    print("4️⃣  🧾 Reporte general del negocio")
    print("5️⃣  🔙 Volver al menú principal")

def exportar_excel(datos, columnas, nombre_archivo):
    if datos:
        fecha = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        ruta_archivo = f"{nombre_archivo}_{fecha}.xlsx"
        df = pd.DataFrame(datos, columns=columnas)
        df.to_excel(ruta_archivo, index=False)
        print(f"✅ Reporte exportado a '{ruta_archivo}'")
    else:
        print("📭 No hay datos para exportar.")

def reporte_inventario():
    conexion = conectarDB()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, cantidad, unidad FROM productos")
            resultados = cursor.fetchall()
            print("\n📦 Reporte de Inventario:")
            if resultados:
                for id, nombre, cantidad, unidad in resultados:
                    print(f"ID: {id} | {nombre} - {cantidad} {unidad}")
                exportar_excel(resultados, ["ID", "Nombre", "Cantidad", "Unidad"], "reporte_inventario")
            else:
                print("📭 Inventario vacío.")
        except Exception as e:
            print(f"❌ Error al generar reporte: {e}")

def reporte_clientes():
    conexion = conectarDB()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, telefono, direccion FROM clientes")
            resultados = cursor.fetchall()
            print("\n👥 Reporte de Clientes:")
            if resultados:
                for id, nombre, telefono, direccion in resultados:
                    print(f"ID: {id} | {nombre} - {telefono} - {direccion}")
                exportar_excel(resultados, ["ID", "Nombre", "Teléfono", "Dirección"], "reporte_clientes")
            else:
                print("📭 No hay clientes registrados.")
        except Exception as e:
            print(f"❌ Error al generar reporte: {e}")

def reporte_proveedores():
    conexion = conectarDB()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, contacto, telefono FROM proveedores")
            resultados = cursor.fetchall()
            print("\n🚚 Reporte de Proveedores:")
            if resultados:
                for id, nombre, contacto, telefono in resultados:
                    print(f"ID: {id} | {nombre} - {contacto} - {telefono}")
                exportar_excel(resultados, ["ID", "Nombre", "Contacto", "Teléfono"], "reporte_proveedores")
            else:
                print("📭 No hay proveedores registrados.")
        except Exception as e:
            print(f"❌ Error al generar reporte: {e}")

def reporte_general():
    conexion = conectarDB()
    if conexion:
        try:
            with pd.ExcelWriter(f"reporte_general_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx") as writer:
                # Inventario
                cursor = conexion.cursor()
                cursor.execute("SELECT id, nombre, cantidad, unidad FROM productos")
                inventario = cursor.fetchall()
                if inventario:
                    pd.DataFrame(inventario, columns=["ID", "Nombre", "Cantidad", "Unidad"]).to_excel(writer, sheet_name="Inventario", index=False)

                # Clientes
                cursor.execute("SELECT id, nombre, telefono, direccion FROM clientes")
                clientes = cursor.fetchall()
                if clientes:
                    pd.DataFrame(clientes, columns=["ID", "Nombre", "Teléfono", "Dirección"]).to_excel(writer, sheet_name="Clientes", index=False)

                # Proveedores
                cursor.execute("SELECT id, nombre, contacto, telefono FROM proveedores")
                proveedores = cursor.fetchall()
                if proveedores:
                    pd.DataFrame(proveedores, columns=["ID", "Nombre", "Contacto", "Teléfono"]).to_excel(writer, sheet_name="Proveedores", index=False)

            print("✅ Reporte general exportado correctamente.")
        except Exception as e:
            print(f"❌ Error al generar reporte general: {e}")

def menu_reportes():
    while True:
        mostrar_menu_reportes()
        opcion = input("\nSeleccione una opción: ").strip()
        if opcion == "1":
            reporte_inventario()
        elif opcion == "2":
            reporte_clientes()
        elif opcion == "3":
            reporte_proveedores()
        elif opcion == "4":
            reporte_general()
        elif opcion == "5":
            break
        input("\nPresione Enter para continuar...")

