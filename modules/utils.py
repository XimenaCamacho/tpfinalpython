from tabulate import tabulate 

# Validación de un número entero positivo (para menú, stock o bajo_stock)
def validar_entero_positivo(valor):
    if valor.isdigit():
        return int(valor)
    else:
        print("Ingreso incorrecto, por favor intente nuevamente.")
    
# Validacion en menu de numero entre 0 y 6
def validar_opcion_menu():
    while True:
        opcion = input("Ingrese la opción deseada: ")
        if validar_entero_positivo(opcion) is not None:
            opcion = int(opcion)
            if 0 <= opcion <= 6:
                return opcion 
            else:
                print("Opción no válida. Por favor, intente nuevamente.")

# Validación de nombres (solo letras y espacios)
def validar_nombre(nombre):
    nombre_valido = True
    for char in nombre:
        if not (char.isalpha() or char.isspace()):  # No es letra ni espacio
            nombre_valido = False
            break
    if not nombre_valido:
        print("El nombre del producto solo puede contener letras y espacios.")
    return nombre_valido
    
# Validación de precio (número entero o flotante positivo)
def validar_precio(precio):
    if precio.isdigit():  # Entero positivo
        return int(precio)
    elif precio.replace('.', '', 1).isdigit() and precio.count('.') == 1:  # Flotante positivo
        return float(precio)
    else:
        print("Precio inválido. Por favor, ingrese un número válido.")

# Funcion de impresion con formato de tabla
def impresion_de_tabla(datos, encabezados_tablas):
    return tabulate(datos, headers = encabezados_tablas, tablefmt = "fancy_grid")
    
# Función de busqueda
def busqueda_producto(dato, productos):
    for producto in productos:
        if producto['nombre'] == dato:
            return producto
    