import sqlite3

def inicializar_base_de_datos():
    """Inicializa la base de datos SQLite, creando el archivo y las tablas si no existen."""
    conexion = sqlite3.connect("inventario.db")  # Conexión a la base de datos (crea el archivo si no existe)
    cursor = conexion.cursor()
    
    # Crear tabla "productos" si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    
    conexion.commit()  # Confirmar cambios
    conexion.close()   # Cerrar la conexión

def get_connection():
    """Devuelve una conexión activa a la base de datos."""
    return sqlite3.connect("inventario.db")