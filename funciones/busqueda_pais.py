from archivos.csv_manager import (
    cargar_paises,
)

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


def datos_limpios(pais_encontrado):
    
    datos = ''

    for pais in pais_encontrado:
        for clave , valor in pais.items():
            datos += (f"{clave.capitalize()}: {str(valor).capitalize()}\n")
    return datos