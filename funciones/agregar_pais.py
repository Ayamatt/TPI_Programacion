from archivos.csv_manager import (
    cargar_paises,
    guardar_paises
)

from validaciones.validaciones import (
    validar_nombre_pais,
    validar_poblacion,
    validar_superficie,
    validar_continente
)

# Vuelve a escribir el dataset con el nuevo país agregado por el usuario al final

def agregar_pais():

    paises = cargar_paises()

    nombre = validar_nombre_pais()
    poblacion = validar_poblacion()
    superficie = validar_superficie()
    continente = validar_continente()

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    for pais in paises:
        if pais['nombre'].lower() == nuevo_pais['nombre'].lower():
            return print("Error: el país ya se encuentra cargado.")

    paises.append(nuevo_pais)

    guardar_paises(paises)

    print("\nPaís agregado correctamente.")