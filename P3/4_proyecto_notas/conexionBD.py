import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'bd_notas'
    )
    cursor = conexion.cursor(buffered=True)
except:
    print(f'En este momento no es posible comunicarse con el sistema, intentelo mas tarde ...')
