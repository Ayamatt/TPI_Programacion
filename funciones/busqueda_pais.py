from archivos.csv_manager import (
    cargar_paises,
)

# Permite buscar un país por su nombre en el dataset

def buscar_pais():

    paises = cargar_paises()

    pais_buscado = input("Ingrese el país que desea buscar: ")
    
    for pais in paises:
        if pais_buscado.lower() in pais['nombre'].lower():
            print(f"=== Información del país ===\n")
            print(f"Nombre: {pais['nombre']}")
            print(f"Población: {pais['poblacion']}")
            print(f"Superficie: {pais['superficie']}")
            print(f"Continente: {pais['continente']}\n")
            return

    return print('No se encontró el país ingresado.')