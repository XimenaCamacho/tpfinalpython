from modules.menu import mostrar_menu
from modules.database import inicializar_base_de_datos  # Importar la función para inicializar la DB

def main():
    # Inicializar la base de datos
    inicializar_base_de_datos()
    
    # Mostrar el menú
    mostrar_menu()

if __name__ == "__main__":
    main()