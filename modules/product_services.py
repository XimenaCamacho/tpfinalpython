from .database import get_connection
from .utils import validar_entero_positivo, validar_nombre, validar_precio
from tabulate import tabulate

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not validar_nombre(nombre):
        return
    precio = input("Precio del producto: ").strip()
    if not validar_precio(precio):
        return
    stock = input("Ingrese cantidad del producto: ").strip()
    if not validar_entero_positivo(stock):
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)", (nombre, float(precio), int(stock)))
        conn.commit()
        print("Producto agregado con éxito.")

def mostrar_productos():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

    if not productos:
        print("No hay productos disponibles.")
        return

    tabla = tabulate(productos, headers=["ID", "Nombre", "Precio", "Stock"], tablefmt="fancy_grid")
    print(tabla)

def actualizar_stock():
    nombre = input("Ingrese el nombre del producto a modificar stock: ").strip()
    if not validar_nombre(nombre):
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE LOWER(nombre) = ?", (nombre.lower(),))
        producto = cursor.fetchone()

    if not producto:
        print("Producto no encontrado.")
        return

    stock = input("Ingrese nueva cantidad del producto: ").strip()
    if not validar_entero_positivo(stock):
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE productos SET stock = ? WHERE id = ?", (int(stock), producto[0]))
        conn.commit()
        print("Stock actualizado con éxito.")
        mostrar_productos()

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
    if not validar_nombre(nombre):
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE LOWER(nombre) = ?", (nombre.lower(),))
        producto = cursor.fetchone()

    if not producto:
        print("Producto no encontrado.")
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (producto[0],))
        conn.commit()
        print("Producto eliminado con éxito.")
        mostrar_productos()

def buscar_producto():
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()
    if not validar_nombre(nombre):
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE LOWER(nombre) = ?", (nombre.lower(),))
        producto = cursor.fetchone()

    if not producto:
        print("Producto no encontrado.")
        return

    tabla = tabulate([producto], headers=["ID", "Nombre", "Precio", "Stock"], tablefmt="fancy_grid")
    print(tabla)

def reporte_bajo_stock():
    stock_bajo = input("Ingrese el número considerado stock bajo: ").strip()
    if not validar_entero_positivo(stock_bajo):
        return

    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos WHERE stock <= ?", (int(stock_bajo),))
        productos = cursor.fetchall()

    if not productos:
        print("No hay productos con stock bajo.")
        return

    tabla = tabulate(productos, headers=["ID", "Nombre", "Precio", "Stock"], tablefmt="fancy_grid")
    print(tabla)


#--------------------   
# Explicación 1:
#--------------------
# Generacion de ID (No es optimo en grandes contenidos de informacion calculo yo, pero me sirve para este tp)
# Encuentra el ID más alto de los productos actuales.
# Asigna el siguiente número como ID del nuevo producto.
# Explicación del codigo:

#   producto["id"] = max([p["id"] for p in products]) + 1:
#      Esta línea recorre la lista de productos (products), extrae los IDs de cada uno (p["id"]), y luego usa la función max() para obtener el valor más alto. 
#      Le suma 1 para asignar el siguiente ID disponible.
#      Si la lista de productos está vacía (if products:), asigna el ID 1 como el primer producto.

#--------------------
# Explicación 2:
#--------------------
# En Python, los objetos que almacenas en una lista (en este caso, los diccionarios que representan productos) son referencias en memoria. 
# Esto significa que cuando buscas un producto con busqueda_producto y obtienes un resultado, estás accediendo directamente al mismo objeto que está almacenado en la lista products.
# Por lo tanto, no necesitas volver a recorrer el array para encontrarlo de nuevo, porque ya tienes una referencia al objeto correcto. 
# Al llamar a products.remove(producto), Python busca ese mismo objeto en la lista (basándose en su referencia en memoria) y lo elimina.
# Analicemos el flujo
# busqueda_producto busca y devuelve un objeto (diccionario) que está dentro de la lista products. Por ejemplo, devuelve algo como:

# {"id": 1, "nombre": "pelota de fútbol", "precio": 1500.00, "stock": 25}

# Cuando asignas el resultado de busqueda_producto a la variable producto, esta variable apunta al mismo diccionario que está dentro de la lista. 
# Es decir, no se crea una copia del diccionario.
# Al ejecutar products.remove(producto), Python internamente busca ese mismo objeto en la lista y lo elimina.
# ¿Qué pasaría si creáramos una copia del objeto?
# Si busqueda_producto devolviera una copia del diccionario en lugar del original, la eliminación fallaría porque remove no encontraría esa copia en la lista.
# Conclusión
# En Python, la referencia al objeto importa. Mientras trabajes con la misma referencia, no necesitas recorrer la lista nuevamente para eliminarlo.

#--------------------
# Explicación 3:
#--------------------
# Usa doble corchete ([[ ]]) en la variable datos porque tabulate espera que la estructura de datos para la tabla sea una lista de listas, donde cada sublista representa una fila de la tabla.
# Si estás mostrando un solo producto, necesitas que esa única fila también esté dentro de una lista. Por eso se usa un par extra de corchetes.
# Si no uso doble corchetes tabulate no funcionará correctamente porque interpretará que cada elemento de la lista corresponde a una columna sin filas, lo cual no es válido.