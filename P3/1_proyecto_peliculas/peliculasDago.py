import mysql.connector
from mysql.connector import Error

pelicula={}


def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n\t...Oprima cualquier tecla para continuar ...")
  input()  

def conectarDB():
  try:
    conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_peliculas"   
    )
    return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None

def crearPeliculas():
  borrarPantalla()
  conexionBd=conectarDB()
  if conexionBd!=None:
    print("\U0001F4DD  .:: Alta de Películas ::. \n")  # 📝
  pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
  pelicula.update({"categoria":input("Ingresa la categoria: ").upper().strip()})
  pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
  pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
  pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
  ############### AGREGAR REGISTRO A LA BASE DE DATOS
  try:
    cursor=conexionBd.cursor()
    sql=(
      "INSERT INTO peliculas (id, nombre, categoria, clasificacion, genero, idioma) VALUES (NULL, %s, %s, %s, %s, %s)"
          #  (
          #      pelicula["nombre"],
          #      pelicula["categoria"],
          #      pelicula["clasificacion"],
          #      pelicula["genero"],
          #      pelicula["idioma"]
          #  )
    )
    val=(pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'])
    
    cursor.execute(sql, val)
    conexionBd.commit()
    print("\n\t\U0001F389 ..:::: La operación se realizó con éxito :::..")  # 🎉
  except Error as e:
    print(f"Erros al intentar insertar un registro en la base de datos {e}")
  
  # cursor.execute("INSERT INTO peliculas {id, nombre, categoria, clasificacion, genero, idioma} VALUES {NULL, %s, %s, %s, %s, %s}, (pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'])")
  
def mostrarPeliculas():
  borrarPantalla()
  conexion=conectarDB()
  
  cursor= conexion.cursor()
  sql=("SELECT * FROM peliculas")
  cursor.execute(sql)
  registros=cursor.fetchall()
  
  if registros:
    print("\n \U0001F50D  .:: Mostrar Películas ::. \n")  # 🔍
    print(f"{'|'}{'id':<10} {'|'}{'nombre':<20} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
    print(f"{'-'*120}")
    for fila in registros:
      print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
  else: 
    print("\t\u274C No hay películas en el sistema.")  # ❌

def borrarPeliculas():
   borrarPantalla()
   conexion=conectarDB()
  
   cursor= conexion.cursor()
   nombre=input("Dame el nombre de la pelicula a borrar: ").lower().strip()
   sql=("SELECT * FROM peliculas where nombre=%s")
   val=(nombre,)
   cursor.execute(sql,val)
   registros=cursor.fetchall()
  
   if registros:
     print("\n \U0001F50D  .:: Mostrar Películas ::. \n")  # 🔍
     print(f"{'|'}{'id':<10} {'|'}{'nombre':<20} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
     print(f"{'-'*120}")
     for fila in registros:
        print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
     resp=input(f"¿Deseas borrar la pelicula de {nombre}? (SI/NO): ").lower().strip()
     if resp=="si":
       sql="DELETE FROM peliculas WHERE nombre=%s"
       val=(nombre, )
       cursor.execute(sql, val)
       conexion.commit()
       input("\n\t..:::: La operacion se realizo con exito::::.. ✅")
     else:
       print("\t..::La accion se canceló con exito::..")
      # print("\n \U0001F50D  .:: Buscar Películas ::. \n")  # 🔍
      # print(f"{'|'}{'id':<8} {'|'}{'nombre':<19} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
      # print(f"{'-'*112}")
      # for fila in registros:
      #   print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
   else: 
      print("\t\u274C Esta a eliminar no se encuentra en el sistema.")  # ❌

def buscarPeliculas():
  borrarPantalla()
  conexion=conectarDB()
  
  cursor= conexion.cursor()
  nombre=input("Dame el nombre de la pelicula a buscar: ").lower().strip()
  sql=("SELECT * FROM peliculas where nombre=%s")
  val=(nombre,)
  cursor.execute(sql,val)
  registros=cursor.fetchall()
  
  if registros:
    print("\n \U0001F50D  .:: Buscar Películas ::. \n")  # 🔍
    print(f"{'|'}{'id':<8} {'|'}{'nombre':<19} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
    print(f"{'-'*112}")
    for fila in registros:
      print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
  else: 
    print("\t\u274C Esta pelicula no existe.")  # ❌

def modificarPeliculas():
  borrarPantalla()
  conexion=conectarDB()
  cursor=conexion.cursor()
  nombre=input("Dame el nombre de la pelicula a modificar: ").lower().strip()
  sql=("SELECT * FROM peliculas where nombre=%s")
  val=(nombre,)
  cursor.execute(sql,val)
  registros=cursor.fetchall()

  if registros:
      print("\n \U0001F50D  .:: Mostrar Películas ::. \n")  # 🔍
      print(f"{'|'}{'id':<10} {'|'}{'nombre':<20} {'|'}{'categoria':<20}{'|'}{'clasificacion':<15}{'|'}{'genero':<16}{'|'}{'idioma':<17}{'|'}")
      print(f"{'-'*120}")
      for fila in registros:
        print(f"{'|'}{fila [0]:<10}{'|'} {fila [1]:<20}{'|'} {fila [2]:<20}{'|'} {fila [3]:<15}{'|'} {fila [4]:<16}{'|'} {fila [5]:<17}{'|'}")
        resp=input(f"¿Deseas actualizar la pelicula de {nombre}? (SI/NO): ").lower().strip()
      if resp=="si":
        pelicula["nombre"]=input("nombre: ").lower().strip()
        pelicula["categoria"]=input("categoria: ").lower().strip()
        pelicula["clasificacion"]=input("clasificacion: ").lower().strip()
        pelicula["genero"]=input("genero: ").lower().strip()
        pelicula["idioma"]=input("idioma: ").lower().strip()
        sql=" UPDATE peliculas SET nombre = %s, categoria = %s, clasificacion = %s, genero = %s, idioma = %s WHERE nombre = %s"
        val=(pelicula['nombre'], pelicula['categoria'], pelicula['clasificacion'], pelicula['genero'], pelicula['idioma'], nombre)
        cursor.execute(sql, val)
        conexion.commit()
        input("\n\t..:::: La operacion se realizo con exito::::.. ✅")
      else:
       print("\t..::La accion se canceló con exito::..")
  else: 
      print("\t\u274C Esta a eliminar no se encuentra en el sistema.")# ❌