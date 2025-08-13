import mysql.connector
from mysql.connector import Error

def conectarDB():
  try:
    conexion=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_proyecto_burger"   
    )
    return conexion
  except Error as e:
    print(f"El error que sucedio es: {e}")
    return None