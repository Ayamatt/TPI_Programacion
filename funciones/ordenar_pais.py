from archivos.csv_manager import cargar_paises
from validaciones.validaciones import validar_opcion_filtro

def ordenar_pais():

    paises = cargar_paises()

    print('Ordenar países por:\n')
    print('1) Nombre')
    print('2) Población')
    print('3) Superficie')

    seleccion_usuario = validar_opcion_filtro()

    #Opción 1
    if seleccion_usuario == 1:
        
        paises_nombre = []

        for pais in paises:
            paises_nombre.append(pais['nombre'])

        paises_sorted = sorted(paises_nombre)

        print("=== Países ordenados por nombre ===\n")
        for pais in paises_sorted:
            print(pais)
            
        print()
        return

    #Opción 2
    elif seleccion_usuario == 2:
        
        paises_poblacion = []

        for pais in paises:
            paises_poblacion.append(pais['poblacion'])

        paises_sorted = sorted(paises_poblacion)

        print("=== Países ordenados por población ===\n")
        for poblacion in paises_sorted:
            for pais in paises:
                if pais['poblacion'] == poblacion:
                    print(f"País: {pais['nombre']} - Población: {pais['poblacion']}")
            
        print()
        return

    #Opción 2
    elif seleccion_usuario == 3:
        
        paises_superficie = []

        for pais in paises:
            paises_superficie.append(pais['superficie'])

        while True:

            opcion = int(input("¿De que manera desea ordenar (1: Ascendente, 2: Descendente)? "))

            if opcion == 1:
                paises_sorted = sorted(paises_superficie)

                print("=== Países ordenados por superficie (Ascendente) ===\n")
                for superficie in paises_sorted:
                    for pais in paises:
                        if pais['superficie'] == superficie:
                            print(f"País: {pais['nombre']} - Superficie: {pais['superficie']}")

                print()
                return

            elif opcion == 2:
                paises_sorted = sorted(paises_superficie, reverse=True)

                print("=== Países ordenados por superficie (Descendente) ===\n")
                for superficie in paises_sorted:
                    for pais in paises:
                        if pais['superficie'] == superficie:
                            print(f"País: {pais['nombre']} - Superficie: {pais['superficie']}")

                print()
                return
            else:
                print("Error: opción inválida.")