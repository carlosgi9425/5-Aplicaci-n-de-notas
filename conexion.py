# Importa el conector
import mysql.connector as mysql

# Crea la conexión
def conectar():
    try:
        conexion = mysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'notas '
        )
        print(' se ha conectado a la base de datos')
        return conexion
    except mysql.Error as err:
        print( ' ha ocurrido un error al conectarse'+ err)