from .product_services import agregar_producto, mostrar_productos, actualizar_stock, eliminar_producto, buscar_producto, reporte_bajo_stock
from .utils import validar_opcion_menu 

def mostrar_menu():
    while True:
        print("=" * 70)
        print("Menu principal.")
        print("=" * 70)
        print("1. Agregar producto.")
        print("2. Mostrar productos.")
        print("3. Actualizar stock de un producto.")
        print("4. Eliminar producto.")
        print("5. Buscar producto.")
        print("6. Reporte de bajo stock.")
        print("0. Salir del programa.")

        opcion = validar_opcion_menu()

        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            mostrar_productos()
        elif opcion == 3:
            actualizar_stock()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            buscar_producto()
        elif opcion == 6:
            reporte_bajo_stock()
        elif opcion == 0:
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        print("=" * 70)