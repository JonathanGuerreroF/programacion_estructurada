from conexionBD import conectarDB
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()

def registrar(nombre, apellidos, email, contrasena):
    try:
        conexion = conectarDB()
        cursor = conexion.cursor()
        fecha = datetime.datetime.now()
        contrasena = hash_password(contrasena)
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password, fecha) VALUES (%s, %s, %s, %s, %s)"
        val = (nombre, apellidos, email, contrasena, fecha)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except Exception as e:
        print("❌ Error al registrar usuario:", e)
        return False

def iniciar_sesion(email, contrasena):
    try:
        conexion = conectarDB()
        cursor = conexion.cursor()
        contrasena = hash_password(contrasena)
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        val = (email, contrasena)
        cursor.execute(sql, val)
        usuario = cursor.fetchone()
        return usuario
    except Exception as e:
        print("❌ Error al iniciar sesión:", e)
        return None
