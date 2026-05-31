from archivos.csv_manager import (
    cargar_paises,
    guardar_paises
)

from validaciones.validaciones import (
    validar_nombre_existente,
    validar_poblacion,
    validar_superficie
)

def actualizar_pais():

    paises = cargar_paises()

    nombre = validar_nombre_existente()

    nueva_poblacion = validar_poblacion()
    nueva_superficie = validar_superficie()

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie
            break

    guardar_paises(paises)

    print("\nPaís actualizado correctamente.")